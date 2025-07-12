import random
import time
from ..helper import clear_screen
from .short_tr import short_tr_QA
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY


def select_question_types():
    question_types = [
        'Multiple Choice (WIP)',
        'Fill in the Blank (WIP)',
        'Fill in the Blank with Options (WIP)',
        'Meaning (WIP)',
        'Pronounciation (WIP)',
        'Short Translation',
        'Long Translation (WIP)'
    ]
    selected_types = []

    while True:

        clear_screen()

        available_types = [q for q in question_types if q not in selected_types]

        print('Select the types of questions you want to include in the test:')
        print('Type the number to select, or 0 to finish.')

        for idx, qtype in enumerate(available_types, 1):
            print(f'{idx}. {qtype}')

        print('0. Finish selection')

        if not available_types:
            print('All question types have been selected.')
            break

        choice = input('Enter your choice: ')

        if choice == '0' or choice.lower() == 'done':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(available_types):
            selected = available_types[int(choice) - 1]
            selected_types.append(selected)
            print(f'Added: {selected}')
        else:
            print('Invalid option. Please try again.')

    return selected_types

def assign_questions(length, selected_question_types):
    try:
        num_questions_int = int(length)
        if num_questions_int <= 0:
            raise ValueError
    except ValueError:
        print('Invalid number of questions. Using 5 as default.')
        num_questions_int = 5

    question_type_list = [random.choice(selected_question_types) for _ in range(num_questions_int)]
    return question_type_list

def generate_questions_and_answers(question_type_list, results, reading_language, target_language, difficulty):
    questions = []
    answers = []
    for idx, qtype in enumerate(question_type_list, start=1):
        start_time = time.time()
        if results:
            palavra, leitura, traducao = random.choice(results)
        else:
            palavra, leitura, traducao = 'exemplo', '', 'exemplo'

        if qtype.startswith('Short Translation'):
            qa = short_tr_QA(
                reading_language,
                target_language,
                traducao,
                difficulty
            )
            questions.append(qa['question'])
            answers.append(qa['answer'])
        else:
            questions.append(f'Question for type: {qtype}')
            answers.append('Answer placeholder')
        elapsed = time.time() - start_time
        print(f'Question {idx}: complete. Time taken: {elapsed:.2f} seconds.')

    return questions, answers

def register_font(nome_fonte="NotoSansJP", arquivo="NotoSansJP-Regular.ttf"):
    pdfmetrics.registerFont(TTFont(nome_fonte, arquivo))

def generate_pdf(lista, nome_arquivo, titulo="", fonte="NotoSansJP"):
    fonte_bold = fonte + "-Bold"
    fonte_regular = fonte + "-Regular"

    # Configurar documento com margens
    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize=A4,
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )
    
    # Criar estilos aprimorados
    styles = getSampleStyleSheet()
    
    # Estilo para título
    estilo_titulo = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        fontName=fonte_bold,
        fontSize=18,
        alignment=1,  # Centralizado
        spaceAfter=14,
        underlineWidth=1,
        underlineOffset=-6,
        underlineGap=4,
    )
    
    # Estilo para itens
    estilo_item = ParagraphStyle(
        'Item',
        parent=styles['BodyText'],
        fontName=fonte_regular,
        fontSize=12,
        leading=16,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        firstLineIndent=0,
        leftIndent=0
    )
    
    # Estilo para número do item
    estilo_numero = ParagraphStyle(
        'Numero',
        parent=estilo_item,
        fontName=fonte_bold
    )
    
    # Conteúdo do PDF
    conteudo = []
    
    # Adicionar título com linha decorativa
    if titulo:
        titulo_paragraph = Paragraph(f"<b>{titulo}</b>", estilo_titulo)
        conteudo.append(titulo_paragraph)
        conteudo.append(Spacer(1, 0.8*cm))

    # Adicionar itens com layout de tabela para melhor alinhamento
    for i, item in enumerate(lista, 1):
        # Usar tabela para garantir alinhamento perfeito
        numero_text = Paragraph(f"<para align='right'><b>{i}.</b></para>", estilo_numero)
        item_text = Paragraph(item, estilo_item)
        
        tabela_item = Table(
            [[numero_text, item_text]],
            colWidths=[1.2*cm, None],
            style=TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ])
        )
        
        conteudo.append(tabela_item)
        conteudo.append(Spacer(1, 0.4*cm))
    
    # Adicionar rodapé profissional
    rodape = Paragraph(
        f"<para align='center' spaceBefore=20 fontName='{fonte_regular}' fontSize=8 "
        f"textColor='#7f8c8d'>Documento gerado em 24/06/2025</para>",
        estilo_item
    )
    conteudo.append(rodape)
    
    # Gerar PDF
    doc.build(conteudo)