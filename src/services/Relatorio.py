from services import GerenciadorTransacoes
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from pathlib import Path
import shutil

def gerar_relatorio(nome_arquivo='Relatorio_transaçoes.pdf'):
    rr = GerenciadorTransacoes.Gerenciador()
    if rr.existe_transacao() is False:
        return

    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize = A4,
        rightMargin=54, leftMargin=54,
        topMargin=54, bottomMargin=54
    )

    elementos = []

    estilos = getSampleStyleSheet()
    titulo_estilo = ParagraphStyle(
        'TituloCustom',
        parent= estilos['Heading1'],
        fontSize= 18, 
        textColor= colors.HexColor('#1A365D'),
        spaceAfter= 10 
    )

    elementos.append(Paragraph('Relatório de Transações Financeiras', titulo_estilo))
    elementos.append(Paragraph('Extrato gerado automaticamente via Python.', estilos['Normal']))
    elementos.append(Spacer(1,15))

    tabela_dados, total_receitas, total_despesas = rr.dados_relatorio()

    tabela = Table(tabela_dados, colWidths= [35, 65, 75, 150, 170])

    estilo_tabela = [
       ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
       ('ALIGN', (4, 1), (4, -1), 'RIGHT'),  
       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
       ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
       ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
       ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')])
    ]

    for i in range(1, len(tabela_dados)):
        tipo_transacao = tabela_dados[i][2]
        cor_texto = colors.HexColor('#22543D') if tipo_transacao == "Receita" else colors.HexColor('#742A2A')
        estilo_tabela.append(('TEXTCOLOR', (2, i), (2, i), cor_texto)) 
        estilo_tabela.append(('FONTNAME', (2, i), (2, i), 'Helvetica-Bold'))

    tabela.setStyle(TableStyle(estilo_tabela))
    elementos.append(tabela)
    elementos.append(Spacer(1, 20))

    saldo_final = total_receitas - total_despesas
    cor_saldo = '#2B6CB0' if saldo_final >= 0 else '#C53030'

    resumo_dados = [
        ["Resumo Geral", ""],
        ["Total de Receitas:", f"R$ {total_receitas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
        ["Total de Despesas:", f"R$ {total_despesas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
        ["Saldo Final:", f"R$ {saldo_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")]
    ]

    tabela_resumo = Table(resumo_dados, colWidths=[150, 154])
    tabela_resumo.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)), 
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#4A5568')),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'RIGHT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#EDF2F7')),
        ('FONTNAME', (0, 3), (1, 3), 'Helvetica-Bold'), 
        ('TEXTCOLOR', (1, 3), (1, 3), colors.HexColor(cor_saldo))
    ]))

    elementos.append(tabela_resumo)

    doc.build(elementos)
    print(f"Relatório gerado com sucesso: {nome_arquivo}")


def baixar_dados():
    arquivo_original = Path("Relatorio_transacoes.pdf")
    
    if not arquivo_original.exists():
        print("Ainda não há nenhum relatório gerado para baixar!")
        return

    pasta_downloads = Path.home() / "Downloads"
    destino = pasta_downloads / "Relatorio_transacoes.pdf"
    
    shutil.copy(arquivo_original, destino)
    print(f"Sucesso! Arquivo copiado para: {destino}")

def exportar_dados():
    pass