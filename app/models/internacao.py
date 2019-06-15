from .model import Model


class Internacao(Model):

    def __init__(self, cpf_paciente, crm_medico, cnpj_hospital, descricao, data_in, data_out):
        self.cpf_paciente = cpf_paciente
        self.crm_medico = crm_medico
        self.cnpj_hospital = cnpj_hospital
        self.descricao = descricao
        self.data_in = data_in
        self.data_out = data_out
