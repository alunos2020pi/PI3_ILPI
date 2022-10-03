from django.contrib import admin
from betel.models import Hospede, Fator_de_Risco_Social, Familiar, Anotacao_de_Enfermagem, Sinais_Vitais, Controle_de_Dextro, Evolucao, Medicacao, Prescricao, Equipe

# Register your models here.

class FamiliarInline(admin.StackedInline):
    model = Familiar
    
class PrescricaoInline(admin.TabularInline):
    model = Prescricao

@admin.register(Fator_de_Risco_Social) 
class Fator_de_Risco_SocialAdmin(admin.ModelAdmin): 
    list_display = ('nome',)

@admin.register(Hospede) 
class HospedeAdmin(admin.ModelAdmin): 
    list_display = ('nome_do_hospede', 'sexo', 'data_de_admissao', 'n_de_matricula', 'data_desligamento_obito', 'nascimento') 
    inlines = [FamiliarInline, PrescricaoInline]

    
@admin.register(Familiar) 
class FamiliarAdmin(admin.ModelAdmin): 
    list_display = ('hospede','nome','data_de_nascimento','parentesco_vinculo') 
    
@admin.register(Equipe) 
class Equipe(admin.ModelAdmin): 
    list_display = (
        'nome', 'data_de_nascimento', 'profissao', 'jornada', 'endereco_rua', 'endereco_numero', 'endereco_complemento',
        'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial', 'telefone_celular', 'telefone_outro',
    ) 

@admin.register(Anotacao_de_Enfermagem) 
class Anotacao_de_Enfermagem(admin.ModelAdmin): 
    list_display = ('hospede','data_hora','anotacao', 'responsavel')
    
@admin.register(Sinais_Vitais) 
class Sinais_Vitais(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'responsavel')
    
@admin.register(Controle_de_Dextro) 
class Controle_de_Dextro(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'dextro', 'responsavel')

@admin.register(Evolucao) 
class Evolucao(admin.ModelAdmin): 
    list_display = ('hospede','data_hora', 'tipo_de_evolucao', 'evolucao', 'responsavel')
    
@admin.register(Medicacao) 
class Medicacao(admin.ModelAdmin): 
    list_display = ('nome','quantidade', 'unidade', 'fabricante', 'generico')
    
@admin.register(Prescricao) 
class Prescricao(admin.ModelAdmin): 
    list_display = (
        'hospede','medicacao', 'dose', 'horario', 'repeticao', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo',
         'data_de_inicio', 'duracao', 'dias_de_duracao', 'data_final', 'data_da_prescricao', 'medico_responsavel',
    )