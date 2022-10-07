from django.contrib import admin
from betel.models import Hospede, Fator_de_Risco_Social, Familiar, Anotacao_de_Enfermagem, Sinais_Vitais, Controle_de_Dextro, Evolucao, Medicacao, Prescricao, Equipe, Enfermidade, Ficha_de_Avaliacao, Item, Estoque

# Register your models here.

class FamiliarInline(admin.StackedInline):
    model = Familiar
    
class PrescricaoInline(admin.TabularInline):
    model = Prescricao
    
class Ficha_de_AvaliacaoInline(admin.StackedInline):
    model = Ficha_de_Avaliacao
    max_num = 1
    
class EstoqueInline(admin.TabularInline):
    model = Estoque    

@admin.register(Fator_de_Risco_Social) 
class Fator_de_Risco_SocialAdmin(admin.ModelAdmin): 
    list_display = ('nome',)

@admin.register(Hospede) 
class HospedeAdmin(admin.ModelAdmin): 
    list_display = ('nome_do_hospede', 'sexo', 'data_de_admissao', 'n_de_matricula', 'data_desligamento_obito', 'nascimento') 
    inlines = [FamiliarInline, PrescricaoInline, Ficha_de_AvaliacaoInline, EstoqueInline]

    
@admin.register(Familiar) 
class FamiliarAdmin(admin.ModelAdmin): 
    list_display = ('hospede','nome','data_de_nascimento','parentesco_vinculo')
    list_filter = ('hospede',)
    
@admin.register(Equipe) 
class EquipeAdmin(admin.ModelAdmin): 
    list_display = (
        'nome', 'data_de_nascimento', 'profissao', 'jornada', 'endereco_rua', 'endereco_numero', 'endereco_complemento',
        'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial', 'telefone_celular', 'telefone_outro',
    ) 

@admin.register(Anotacao_de_Enfermagem) 
class Anotacao_de_EnfermagemAdmin(admin.ModelAdmin): 
    list_display = ('hospede','data_hora','anotacao', 'responsavel')
    list_filter = ('hospede','data_hora')
    
@admin.register(Sinais_Vitais) 
class Sinais_VitaisAdmin(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'responsavel')
    list_filter = ('hospede', 'data_hora',)
    
@admin.register(Controle_de_Dextro) 
class Controle_de_DextroAdmin(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'dextro', 'responsavel')
    list_filter = ('hospede','data_hora')

@admin.register(Evolucao) 
class EvolucaoAdmin(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'tipo_de_evolucao', 'evolucao', 'responsavel')
    list_filter = ('hospede', 'data_hora', 'tipo_de_evolucao',)
    
@admin.register(Medicacao) 
class MedicacaoAdmin(admin.ModelAdmin): 
    list_display = ('nome','quantidade', 'unidade', 'fabricante', 'generico')
    
@admin.register(Prescricao) 
class PrescricaoAdmin(admin.ModelAdmin): 
    list_display = (
        'hospede','medicacao', 'dose', 'horario', 'repeticao', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo',
         'data_de_inicio', 'duracao', 'dias_de_duracao', 'data_final', 'data_da_prescricao', 'medico_responsavel',
    )
    
@admin.register(Enfermidade) 
class EnfermidadeAdmin(admin.ModelAdmin): 
    list_display = ('nome',)
    
@admin.register(Ficha_de_Avaliacao) 
class Ficha_de_AvaliacaoAdmin(admin.ModelAdmin): 
    list_display = ('hospede', )
    
@admin.register(Item) 
class ItemAdmin(admin.ModelAdmin): 
    list_display = ('nome', )  
    
@admin.register(Estoque) 
class EstoqueAdmin(admin.ModelAdmin): 
    list_display = ('hospede', 'item', 'quantidade' )
    list_filter = ('hospede',)    