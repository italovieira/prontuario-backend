from .model import Model

from ..util import format_date


class Internacao(Model):

    def __init__(self, cpf_paciente, crm_medico, cnpj_hospital, descricao, data_in, data_out):
        self.cpf_paciente = cpf_paciente
        self.crm_medico = crm_medico
        self.cnpj_hospital = cnpj_hospital
        self.descricao = descricao
        self.data_in = format_date(data_in)
        self.data_out = format_date(data_out)
