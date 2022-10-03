from django.db import models

# Create your models here.

class Hospede(models.Model): 
    nome_do_hospede = models.CharField(max_length=50, null=True, blank=True, help_text='Insira o nome do hóspede') 

    SEXO = (
        ('M',	'Masculino'),
        ('F',	'Feminino'),
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        null=True,
        blank=True
    )
    data_de_admissao = models.DateField(null=True, blank=True)
    n_de_matricula = models.CharField(max_length=12, null=True, blank=True)
    data_desligamento_obito = models.DateField(null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    n_bdc = models.CharField(max_length=20, null=True, blank=True)
    n_nis = models.CharField(max_length=20, null=True, blank=True)
    n_cns_sus = models.CharField(max_length=20, null=True, blank=True)
    
    MOTIVO_DA_HOSPEDAGEM = (
        ('AB',	'Abandono'),
        ('AU',	'Ausência de familiares'),
        ('OB',	'Óbito do responsável'),
        ('MU',	'Mudança de endereço'),
        ('OU',	'Outro'),
    )
    
    motivo_da_hospedagem = models.CharField(
        max_length=2,
        choices=MOTIVO_DA_HOSPEDAGEM,
        null=True, blank=True
    )
    
    PROCEDENCIA = (
        ('CA',	'Casa'),
        ('HO',	'Hospital'),
        ('LI',	'Lar de Idosos'),
        ('OU',	'Outro'),
    )
    
    procedencia = models.CharField(
        max_length=2,
        choices=PROCEDENCIA,
        null=True, blank=True
    )
    
    naturalidade_municipio = models.CharField(max_length=20, null=True, blank=True)
    
    ESTADOS = (
        ('AC',	'Acre'),
        ('AL',	'Alagoas'),
        ('AP',	'Amapá'),
        ('AM',	'Amazonas'),
        ('BA',	'Bahia'),
        ('CE',	'Ceará'),
        ('DF',	'Distrito Federal'),
        ('ES',	'Espírito Santo'),
        ('GO',	'Goiás'),
        ('MA',	'Maranhão'),
        ('MT',	'Mato Grosso'),
        ('MS',	'Mato Grosso do Sul'),
        ('MG',	'Minas Gerais'),
        ('PA',	'Pará'),
        ('PB',	'Paraíba'),
        ('PR',	'Paraná'),
        ('PE',	'Pernambuco'),
        ('PI',	'Piauí'),
        ('RJ',	'Rio de Janeiro'),
        ('RN',	'Rio Grande do Norte'),
        ('RS',	'Rio Grande do Sul'),
        ('RO',	'Rondônia'),
        ('RR',	'Roraima'),
        ('SC',	'Santa Catarina'),
        ('SP',	'São Paulo'),
        ('SE',	'Sergipe'),
        ('TO',	'Tocantins'),
    )
    
    naturalidade_estado = models.CharField(
        max_length=2,
        choices=ESTADOS,
        null=True, blank=True
    )
    
    COR_RACA = (
        ('BR',	'Branca'),
        ('PR',	'Preta'),
        ('AM',	'Amarela'),
        ('PA',	'Parda'),
        ('IN',	'Indígena'),
        ('SD',	'Sem Declaração'),
    )
    
    cor_raca = models.CharField(
        max_length=2,
        choices=COR_RACA,
        null=True, blank=True
    )
    
    pessoa_com_deficiencia = models.BooleanField(null=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    rg_emissao = models.DateField(null=True, blank=True)
    rg_orgao_emissor = models.CharField(max_length=20, null=True, blank=True)
    rg_uf = models.CharField(
        max_length=2,
        choices=ESTADOS,
        null=True, blank=True
    )
    
    certidao_de_nascimento_folha = models.PositiveIntegerField(null=True, blank=True)
    certidao_de_nascimento_livro = models.PositiveIntegerField(null=True, blank=True)
    mae = models.CharField(max_length=50, help_text='Insira o nome da mãe', null=True, blank=True)
    pai = models.CharField(max_length=50, help_text='Insira o nome do pai', null=True, blank=True)
    nome_do_responsavel = models.CharField(max_length=50, help_text='Insira o nome do responsável', null=True, blank=True)
    grau_de_parentesco = models.CharField(max_length=20, null=True, blank=True)
    
    ESTADO_CIVIL = (
        ('SO',	'Solteiro(a)'),
        ('CA',	'Casado(a)'),
        ('SE',	'Separado(a)'),
        ('DI',	'Divorciado(a)'),
        ('VI',	'Viúvo(a)'),
    )
 
    estado_civil = models.CharField(
        max_length=2,
        choices=ESTADO_CIVIL,
        null=True, blank=True
    )
    
    GRAU_DE_INSTRUCAO = (
        ('EFI',	'Ensino Fundamental Incompleto'),
        ('EFC',	'Ensino Fundamental Completo'),
        ('EMI',	'Ensino Médio Incompleto'),
        ('EMC',	'Ensino Médio Completo'),
        ('ESI',	'Ensino Superior Incompleto'),
        ('ESC',	'Ensino Superior Completo'),
    )
    
    grau_de_instrucao = models.CharField(
        max_length=3,
        choices=GRAU_DE_INSTRUCAO,
        null=True, blank=True
    )
    
    profissao = models.CharField(max_length=20, null=True, blank=True)
    ocupacao = models.CharField(max_length=20, null=True, blank=True)
    
    ESTADO_PROFISSIONAL = (
        ('EM',	'Empregado(a)'),
        ('DE',	'Desempregado(a)'),
        ('AP',	'Aposentado(a)'),
        ('PE',	'Pensionista'),
    )
    
    estado_profissional = models.CharField(
        max_length=2,
        choices=ESTADO_PROFISSIONAL,
        null=True, blank=True
    )
    
    endereco_rua = models.CharField(max_length=20, null=True, blank=True)
    endereco_numero = models.PositiveIntegerField(null=True, blank=True)
    endereco_complemento = models.CharField(max_length=10, null=True, blank=True)
    endereco_cep = models.CharField(max_length=9, help_text='Formato: 00000-000', null=True, blank=True)
    endereco_bairro = models.CharField(max_length=20, null=True, blank=True)
    endereco_distrito = models.CharField(max_length=20, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    telefone_celular = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    telefone_outro = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    ponto_de_referencia = models.CharField(max_length=20, null=True, blank=True)
    
    CONDICOES_DE_MORADIA = (
        ('P',	'Própria'),
        ('A',	'Alugada'),
        ('C',	'Cedida'),
    )
    
    condicoes_de_moradia = models.CharField(
        max_length=1,
        choices=CONDICOES_DE_MORADIA,
        null=True, blank=True
    ) 
    
    n_de_comodos = models.PositiveIntegerField(null=True, blank=True)
    valor_aluguel_ou_financiamento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    TIPO_DE_CONSTRUCAO = (
        ('AL',	'Alvenaria'),
        ('MA',	'Madeira'),
        ('MI',	'Mista'),
    )
    
    tipo_de_construcao = models.CharField(
        max_length=2,
        choices=TIPO_DE_CONSTRUCAO,
        null=True, blank=True
    )
    
    SITUACAO_HABITACIONAL = (
        ('CO',	'Cortiço'),
        ('FA',	'Favela'),
        ('LI',	'Loteamento Irregular'),
    )
    
    situacao_habitacional = models.CharField(
        max_length=2,
        choices=SITUACAO_HABITACIONAL,
        null=True, blank=True
    )
    
    RECEBE_PROGRAMA_DE_TRANSFERENCIA_DE_RENDA = (
        ('NR',	'Não Recebe'),
        ('SB',	'Sim, BPC'),
        ('BF',	'Sim, Bolsa Família'),
        ('SL',  'Sim, LOAS'),
        ('SO',  'Sim, Outros'),
    )
    recebe_programa_de_transferencia_de_renda = models.CharField(
        max_length=2,
        choices= RECEBE_PROGRAMA_DE_TRANSFERENCIA_DE_RENDA,
        null=True, blank=True
    )
    
    recebe_13_salario = models.BooleanField(null=True)
    parcela1_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parcela2_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    RECEBE_BENEFICIO_DE_PRESTACAO_CONTINUADA = (
        ('NR',	'Não Recebe'),
        ('SI',	'Sim, Idoso'),
        ('SP',	'Sim, Pessoa com deficiência'),
    )
    recebe_beneficio_de_prestacao_continuada = models.CharField(
        max_length=2,
        choices= RECEBE_BENEFICIO_DE_PRESTACAO_CONTINUADA,
        null=True, blank=True
    )
    
    possui_convenio_medico = models.BooleanField(null=True)
    qual_convenio = models.CharField(max_length=20, null=True, blank=True)
    
    idoso_recebe_auxilio_para_custo_de_despesas = models.BooleanField(null=True)
    qual_auxilio = models.CharField(max_length=20, null=True, blank=True)
    demanda_apresentada_orientacoes_encaminhamentos = models.CharField(max_length=255, null=True, blank=True)
    assistente_social = models.CharField(max_length=50, null=True, blank=True)
    data_de_preenchimento_da_ficha = models.DateField(null=True, blank=True)
    
 
    class Meta: 
        ordering = ['nome_do_hospede'] 

    def __str__(self): 
        return self.nome_do_hospede 

class Fator_de_Risco_Social(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self): 
        return self.nome

    
class Familiar(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, help_text='Insira o nome do familiar', null=True, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    parentesco_vinculo = models.CharField(max_length=20, null=True, blank=True)
    profissao = models.CharField(max_length=20, null=True, blank=True)
    ocupacao = models.CharField(max_length=20, null=True, blank=True)
    renda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fatores_de_risco_social = models.ManyToManyField(Fator_de_Risco_Social, help_text='Selecione os fatores de risco')
    estuda = models.BooleanField(null=True)
    
    GRAU_DE_INSTRUCAO = (
        ('EFI',	'Ensino Fundamental Incompleto'),
        ('EFC',	'Ensino Fundamental Completo'),
        ('EMI',	'Ensino Médio Incompleto'),
        ('EMC',	'Ensino Médio Completo'),
        ('ESI',	'Ensino Superior Incompleto'),
        ('ESC',	'Ensino Superior Completo'),
    )
    
    grau_de_instrucao = models.CharField(
        max_length=3,
        choices=GRAU_DE_INSTRUCAO,
        null=True, blank=True
    )
    
    inserido_em_ilpi = models.BooleanField(null=True)
    inserido_em_cedesp = models.BooleanField(null=True)
    inserido_em_nci = models.BooleanField(null=True)

 
    class Meta: 

        ordering = ['hospede', 'nome'] 

    def __str__(self): 

        return f'{self.hospede} -> {self.nome}' 
        
class Equipe(models.Model):
    nome = models.CharField(max_length=50, help_text='Insira o nome', null=True, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    profissao = models.CharField(max_length=20, null=True, blank=True)

    JORNADA = (
        ('12/36', '12h por 36h'),
        ('6/1', '6d por 1d'),
        ('NI', 'Não informado')
    
    )
    
    jornada = models.CharField(
        max_length=5,
        choices=JORNADA,
        null=True, blank=True
    )
    
    endereco_rua = models.CharField(max_length=20, null=True, blank=True)
    endereco_numero = models.PositiveIntegerField(null=True, blank=True)
    endereco_complemento = models.CharField(max_length=10, null=True, blank=True)
    endereco_cep = models.CharField(max_length=9, help_text='Formato: 00000-000', null=True, blank=True)
    endereco_bairro = models.CharField(max_length=20, null=True, blank=True)
    endereco_distrito = models.CharField(max_length=20, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    telefone_celular = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    telefone_outro = models.CharField(max_length=20, help_text='Formato: (00)00000-0000', null=True, blank=True)
    
    def __str__(self): 
        return self.nome

class Anotacao_de_Enfermagem(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=True, blank=True)
    anotacao = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.ForeignKey('Equipe', on_delete=models.SET_NULL, blank=True, null=True,)
    
    def __str__(self):
        return f'{self.hospede} -> {self.data_hora}'
    
class Sinais_Vitais(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=True, blank=True)
    pa = models.CharField(max_length=20, null=True, blank=True)
    pulso = models.CharField(max_length=20, null=True, blank=True)
    resp = models.CharField(max_length=20, null=True, blank=True)
    temp = models.CharField(max_length=20, null=True, blank=True)
    sat = models.CharField(max_length=20, null=True, blank=True)
    diures = models.CharField(max_length=20, null=True, blank=True)
    evacuacao = models.CharField(max_length=20, null=True, blank=True)
    responsavel = models.ForeignKey('Equipe', on_delete=models.SET_NULL, blank=True, null=True,)
    
    def __str__(self):
        return f'{self.hospede} -> {self.data_hora}'
    
class Controle_de_Dextro(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=True, blank=True)
    dextro = models.CharField(max_length=20, null=True, blank=True)
    responsavel = models.ForeignKey('Equipe', on_delete=models.SET_NULL, blank=True, null=True,)
    
    def __str__(self):
        return f'{self.hospede} -> {self.data_hora}'
    
class Evolucao(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=True, blank=True)

    TIPO_DE_EVOLUCAO = (
        ('EN',	'Enfermagem'),
        ('FI',	'Fisioterapeutica'),
        ('NU',	'Nutrição'),
        ('ME',  'Médica'),
    )
    
    tipo_de_evolucao = models.CharField(
        max_length=2,
        choices= TIPO_DE_EVOLUCAO,
        null=True, blank=True
    )
    
    evolucao = models.TextField(max_length=500, null=True, blank=True) 
    responsavel = models.ForeignKey('Equipe', on_delete=models.SET_NULL, blank=True, null=True,)
    
    def __str__(self):
        return f'{self.hospede} -> {self.data_hora}'

class Medicacao(models.Model):
    nome = models.CharField(max_length=50, help_text='Insira o nome do remédio', null=True, blank=True)
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    
    UNIDADE = (
        ('mg',	'miligrama'),
        ('UI',	'Unidades Internacionais'),
    )
    
    unidade = models.CharField(
        max_length=10,
        choices= UNIDADE,
        null=True, blank=True
    )
    
    fabricante = models.CharField(max_length=25, null=True, blank=True)
    generico = models.BooleanField(null=True)
    
    def __str__(self):
        return f'{self.nome}, {self.quantidade} {self.unidade} - {self.fabricante} Genérico? {self.generico}'
    
class Prescricao(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    medicacao = models.ForeignKey('Medicacao', on_delete=models.CASCADE)
    dose = models.FloatField(null=True, blank=True)
    horario = models.TimeField(null=True, blank=True)
    
    REPETICAO = (
        ('D', 'Diária'),
        ('S', 'Semanal'),
        ('M', 'Mensal'),
        ('A', 'Anual'),
        ('N', 'Não se repete'),
    )
    
    repeticao = models.CharField(
        max_length=1,
        choices= REPETICAO,
        null=True, blank=True,
    )
    
    segunda = models.BooleanField(null=True)
    terca = models.BooleanField(null=True)
    quarta = models.BooleanField(null=True)
    quinta = models.BooleanField(null=True)
    sexta = models.BooleanField(null=True)
    sabado = models.BooleanField(null=True)
    domingo = models.BooleanField(null=True)
    
    
    data_de_inicio = models.DateField(null=True, blank=True)
    
    
    DURACAO = (
        ('CON',	'Contínua'),
        ('DUR',	'Durante...'),
        ('ATE',	'Até a data'),
    
    )
    
    duracao = models.CharField(
        max_length=3,
        choices=DURACAO,
        null=True, blank=True
    )
    
    dias_de_duracao = models.PositiveIntegerField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    
    data_da_prescricao = models.DateField(null=True, blank=True)
    medico_responsavel = models.ForeignKey('Equipe', on_delete=models.SET_NULL, blank=True, null=True,)
  
    
    def __str__(self):
        return f'{self.hospede} -> {self.medicacao}'
    
    