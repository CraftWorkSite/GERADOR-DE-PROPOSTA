# -*- coding: utf-8 -*-

import datetime
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

# --- DADOS DA SUA EMPRESA (PROPONENTE) ---
PROPONENTE = {
    "empresa": "Craft Work Site",
    "responsavel": "Fagner Ribeiro de Freitas",
    "cnpj": "61.571.293/0001-51",
    "whatsapp": "(43) 9 8447-1575",
    "email": "craftworksite@gmail.com",
    "website": "https://craftworksite.com",
    "cidade_estado": "Apucarana - PR"
}

# --- DEFINIÇÃO DOS PLANOS ---
PLANOS = {
    "1": {
        "nome": "Plano Básico",
        "preco": "1.000,00",
        "slogan": "Ideal para pequenas empresas que querem brilhar!",
        "objetivo": "Desenvolver um site institucional de página única (one-page) para estabelecer uma presença online inicial, focada em apresentar a empresa, seus serviços e informações de contato de forma clara e direta.",
        "incluso_lista": [ "- Página institucional única (One-Page)", "- Layout moderno e responsivo", "- Domínio (.com.br) grátis por 1 ano", "- Hospedagem gratuita (GitHub Pages)", "- Certificado SSL (https) via Cloudflare", "- Botão de contato para WhatsApp", "- Suporte técnico por 30 dias", "- Vídeo tutorial de como solicitar alterações" ],
        "tabela_funcionalidades": [ ['Funcionalidade', 'Descrição'], ['Layout responsivo', 'Compatível com celular, tablet e computador.'], ['Seção "Quem Somos"', 'Apresentação da sua empresa e história.'], ['Seção "Serviços"', 'Descrição dos serviços ou produtos oferecidos.'], ['Seção "Contato"', 'Formulário simples e informações de contato.'], ['Certificado SSL', 'Segurança básica para os visitantes do site.'] ],
        "detalhes_hospedagem": [ "A hospedagem será feita através do GitHub Pages, uma solução robusta e gratuita, ideal para sites estáticos.", "- Custo zero de hospedagem.", "- Alta disponibilidade e velocidade global.", "- Manutenção simplificada." ]
    },
    "2": {
        "nome": "Plano Avançado",
        "preco": "1.499,00",
        "slogan": "Perfeito para negócios em crescimento e ambiciosos!",
        "objetivo": "Desenvolver um site institucional completo em WordPress, com múltiplas páginas, layout profissional e e-mail profissional, permitindo que o cliente gerencie o conteúdo facilmente e fortaleça a imagem da marca.",
        "incluso_lista": [ "- Site institucional completo (até 5 páginas)", "- Layout moderno e responsivo em WordPress", "- Registro de domínio (.com.br) grátis por 1 ano", "- Hospedagem profissional (HostGator - Plano P) grátis por 1 ano", "- Certificado SSL (https)", "- Até 5 contas de E-mail profissional (ex: contato@seusite.com.br)", "- Backups diários automáticos", "- Suporte técnico por 90 dias", "- Vídeo tutorial de uso do painel", "- Painel administrativo para gerenciamento de conteúdo" ],
        "tabela_funcionalidades": [ ['Funcionalidade', 'Descrição'], ['Layout moderno e responsivo', 'Compatível com celular, tablet e computador.'], ['Painel de administração', 'Área simples para gerenciar todo o site (WordPress).'], ['Página de produtos/serviços', 'Com fotos, descrições e categorias.'], ['Página Institucional', 'Quem somos, política de trocas, contatos.'], ['Blog', 'Área para publicação de notícias e artigos.'], ['E-mails profissionais', 'Contas de e-mail com o seu domínio.'], ['Certificado SSL (https)', 'Segurança para os dados dos seus clientes.'] ],
        "detalhes_hospedagem": [ "A hospedagem profissional (grátis no primeiro ano) oferece os seguintes recursos:", "- Hospedagem gerenciada para WordPress", "- Domínio grátis (1º ano)", "- Alto desempenho e estabilidade", "- 100 GB de armazenamento SSD", "- Certificado SSL grátis", "- E-mail grátis (contas ilimitadas)", "- Backups diários" ]
    },
    "3": {
        "nome": "Plano Premium",
        "preco": "2.499,00",
        "slogan": "Para quem quer o melhor e não aceita menos!",
        "objetivo": "Desenvolver uma loja virtual (e-commerce) completa e robusta, com sistema de carrinho de compras, cadastro de produtos e integração com meios de pagamento, pronta para vender online e escalar o negócio.",
        "incluso_lista": [ "- Loja virtual completa (E-commerce)", "- Layout moderno e responsivo (WordPress + WooCommerce)", "- Registro de domínio (.com.br) grátis por 1 ano", "- Hospedagem profissional (HostGator - Plano M) grátis por 1 ano", "- Certificado SSL (https)", "- E-mails profissionais ilimitados", "- Cadastro inicial de até 20 produtos", "- Integração com Correios e meios de pagamento (Mercado Pago, PagSeguro)", "- Carrinho de compras e checkout otimizado", "- Suporte técnico por 120 dias", "- Vídeo tutorial completo de gerenciamento da loja", "- Painel administrativo para gestão de produtos, pedidos e clientes" ],
        "tabela_funcionalidades": [ ['Funcionalidade', 'Descrição'], ['Layout moderno e responsivo', 'Compatível com celular, tablet e computador.'], ['Carrinho de Compras', 'Sistema completo para o cliente adicionar produtos.'], ['Cadastro de Produtos', 'Painel para gerenciar produtos, estoque, preços e fotos.'], ['Gestão de Pedidos', 'Acompanhe e gerencie todas as vendas realizadas.'], ['Integração de Pagamento', 'Aceite pagamentos via cartão de crédito, Pix e boleto.'], ['Cálculo de Frete', 'Cálculo automático integrado com os Correios.'], ['E-mails profissionais', 'Contas de e-mail com o seu domínio.'], ['Certificado SSL (https)', 'Segurança total para as transações dos seus clientes.'] ],
        "detalhes_hospedagem": [ "A hospedagem profissional para e-commerce (grátis no primeiro ano) oferece:", "- Hospedagem otimizada para WooCommerce", "- Domínio grátis (1º ano)", "- Desempenho superior para lojas virtuais", "- Armazenamento SSD para carregamento rápido", "- Certificado SSL dedicado grátis", "- E-mail grátis (contas ilimitadas)", "- Backups diários e restauração fácil" ]
    }
}

# --- FUNÇÕES AUXILIARES E DE ESTILO ---
def get_estilos():
    estilos = getSampleStyleSheet()
    normal_style = estilos['Normal']
    normal_style.fontName = 'Helvetica'
    normal_style.fontSize = 10
    normal_style.leading = 14
    normal_style.alignment = TA_LEFT
    estilos.add(ParagraphStyle(name='Titulo', fontName='Helvetica-Bold', fontSize=22, alignment=TA_CENTER, spaceAfter=20))
    estilos.add(ParagraphStyle(name='Cabecalho1', fontName='Helvetica-Bold', fontSize=14, spaceBefore=20, spaceAfter=10))
    estilos.add(ParagraphStyle(name='Cabecalho2', fontName='Helvetica-Bold', fontSize=11, spaceAfter=5))
    estilos.add(ParagraphStyle(name='Slogan', fontName='Helvetica-Oblique', fontSize=10, alignment=TA_CENTER, spaceAfter=15))
    estilos.add(ParagraphStyle(name='Lista', fontName='Helvetica', fontSize=10, leading=14, leftIndent=20))
    return estilos

def draw_border(canvas, doc):
    canvas.saveState()
    margin_x, margin_y = 1.5 * cm, 1.5 * cm
    page_width, page_height = A4
    x, y, width, height = margin_x, margin_y, page_width - (2 * margin_x), page_height - (2 * margin_y)
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(2)
    canvas.rect(x, y, width, height)
    canvas.restoreState()

# *** NOVA FUNÇÃO PARA O RODAPÉ ***
def footer_com_logo(canvas, doc):
    """
    Desenha a borda e o logo no rodapé para a segunda página em diante.
    """
    # 1. Desenha a borda da página, como antes
    draw_border(canvas, doc)
    
    # 2. Desenha o logo no rodapé
    canvas.saveState()
    
    # Verifica se o logo existe para evitar erros
    if os.path.exists('logo.png'):
        logo_path = 'logo.png'
        logo_width = 2 * cm
        logo_height = 2 * cm
        
        # Pega as dimensões da página
        page_width, page_height = A4
        
        # Calcula a posição (x, y) do logo no canto inferior direito
        # x: Largura da página - margem direita do conteúdo - largura do logo
        x = page_width - (2.5 * cm) - logo_width
        # y: Margem inferior do conteúdo
        y = 2.5 * cm
        
        canvas.drawImage(logo_path, x, y, width=logo_width, height=logo_height, mask='auto')
        
    canvas.restoreState()


# --- FUNÇÃO PRINCIPAL DE GERAÇÃO DO PDF ---
def gerar_proposta(plano_escolhido, nome_cliente, cpf_cnpj_cliente, telefone_cliente):
    plano_info = PLANOS[plano_escolhido]
    nome_arquivo = f"Proposta_Comercial_{nome_cliente.replace(' ', '_')}.pdf"
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4, rightMargin=2.5*cm, leftMargin=2.5*cm, topMargin=2.5*cm, bottomMargin=2.5*cm)
    story = []
    estilos = get_estilos()

    # --- PÁGINA 1 ---
    if os.path.exists('logo.png'):
        logo = Image('logo.png', width=2.5*cm, height=2.5*cm)
        story.append(logo)
    else:
        print("\nAVISO: Arquivo 'logo.png' não encontrado. O PDF será gerado sem o logo.")

    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("PROPOSTA COMERCIAL", estilos['Titulo']))
    story.append(Paragraph(plano_info['nome'], estilos['Cabecalho1']))
    story.append(Paragraph(plano_info['slogan'], estilos['Slogan']))
    data_proponente_cliente = [
        [Paragraph("<b>PROPONENTE</b>", estilos['Cabecalho2']), Paragraph("<b>CLIENTE</b>", estilos['Cabecalho2'])],
        [
            Paragraph(f"{PROPONENTE['empresa']}<br/><b>Responsável:</b> {PROPONENTE['responsavel']}<br/><b>CNPJ:</b> {PROPONENTE['cnpj']}<br/><b>WhatsApp:</b> {PROPONENTE['whatsapp']}<br/><b>E-mail:</b> {PROPONENTE['email']}<br/><b>Website:</b> {PROPONENTE['website']}", estilos['Normal']),
            Paragraph(f"<b>Nome:</b> {nome_cliente}<br/><b>CPF/CNPJ:</b> {cpf_cnpj_cliente}<br/><b>Telefone:</b> {telefone_cliente}", estilos['Normal'])
        ]
    ]
    tabela_proponente_cliente = Table(data_proponente_cliente, colWidths=[8*cm, 8*cm])
    tabela_proponente_cliente.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LINEABOVE', (0, 1), (1, 1), 1, colors.orange), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),]))
    story.append(tabela_proponente_cliente)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("1. Objetivo da Proposta", estilos['Cabecalho1']))
    story.append(Paragraph(plano_info['objetivo'], estilos['Normal']))
    story.append(Paragraph("2. O Que Está Incluso", estilos['Cabecalho1']))
    for item in plano_info['incluso_lista']:
        story.append(Paragraph(item, estilos['Lista']))
    story.append(PageBreak())

    # --- PÁGINA 2 ---
    story.append(Paragraph("3. Detalhes das Funcionalidades", estilos['Cabecalho1']))
    tabela_func = Table(plano_info['tabela_funcionalidades'])
    tabela_func.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFD700')), ('TEXTCOLOR', (0, 0), (-1, 0), colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke), ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    story.append(tabela_func)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("4. Detalhes Técnicos da Hospedagem", estilos['Cabecalho1']))
    for detalhe in plano_info['detalhes_hospedagem']:
        story.append(Paragraph(detalhe, estilos['Normal']))
    story.append(PageBreak())

    # --- PÁGINA 3 ---
    story.append(Paragraph("5. Formas de Pagamento", estilos['Cabecalho1']))
    story.append(Paragraph(f"<b>Valor total:</b> R$ {plano_info['preco']}", estilos['Normal']))
    story.append(Paragraph("<b>Forma de pagamento:</b> À vista via Pix ou cartão de crédito em até 2x sem juros.", estilos['Normal']))
    story.append(Paragraph("6. Prazo e Validade", estilos['Cabecalho1']))
    story.append(Paragraph("<b>Entrega estimada:</b> até 7 dias úteis após o envio dos materiais necessários (logos, textos, fotos, descrição dos produtos, etc.).", estilos['Normal']))
    story.append(Paragraph("<b>Validade desta proposta:</b> 15 dias.", estilos['Normal']))
    story.append(Spacer(1, 2*cm))
    data_atual = datetime.datetime.now().strftime("%d de %B de %Y")
    cidade_data = f"{PROPONENTE['cidade_estado']}, {data_atual.replace('January', 'Janeiro').replace('February', 'Fevereiro').replace('March', 'Março').replace('April', 'Abril').replace('May', 'Maio').replace('June', 'Junho').replace('July', 'Julho').replace('August', 'Agosto').replace('September', 'Setembro').replace('October', 'Outubro').replace('November', 'Novembro').replace('December', 'Dezembro')}"
    story.append(Paragraph(cidade_data, estilos['Normal']))
    story.append(Spacer(1, 3*cm))
    data_assinaturas = [[Paragraph(f"{PROPONENTE['responsavel']}<br/>{PROPONENTE['empresa']}", estilos['Normal']), Paragraph(f"{nome_cliente}<br/>Cliente", estilos['Normal'])]]
    tabela_assinaturas = Table(data_assinaturas, colWidths=[8*cm, 8*cm])
    tabela_assinaturas.setStyle(TableStyle([('LINEABOVE', (0, 0), (0, 0), 1, colors.black, None, (20, 0)), ('LINEABOVE', (1, 0), (1, 0), 1, colors.black, None, (20, 0)), ('ALIGN', (0,0), (-1,-1), 'CENTER'),]))
    story.append(tabela_assinaturas)
    
    # *** LOGO NO FINAL DO CONTEÚDO FOI REMOVIDO DAQUI ***
    
    # *** CONSTRUÇÃO DO PDF ATUALIZADA ***
    # onFirstPage: Função para a primeira página
    # onLaterPages: Função para todas as outras páginas
    doc.build(story, onFirstPage=draw_border, onLaterPages=footer_com_logo)
    print(f"\n✅ Proposta gerada com sucesso! Arquivo: {nome_arquivo}")

# --- INTERFACE COM O USUÁRIO ---
if __name__ == "__main__":
    print("--- Gerador de Proposta Comercial ---")
    print("\n--- Dados do Cliente ---")
    cliente_nome = input("Nome completo do cliente: ")
    cliente_cpf_cnpj = input("CPF ou CNPJ do cliente: ")
    cliente_telefone = input("Telefone do cliente (com DDD): ")
    print("\n--- Escolha um dos planos ---")
    print("1: Plano Básico (R$ 1.000,00) - Site de página única, hospedagem no GitHub.")
    print("2: Plano Avançado (R$ 1.499,00) - Site WordPress com e-mail profissional.")
    print("3: Plano Premium (R$ 2.499,00) - E-commerce completo com carrinho de compras.")
    escolha = ""
    while escolha not in ["1", "2", "3"]:
        escolha = input("Digite o número do plano desejado (1, 2 ou 3): ")
    gerar_proposta(escolha, cliente_nome, cliente_cpf_cnpj, cliente_telefone)
