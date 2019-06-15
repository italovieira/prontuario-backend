from .dao.usuario import UsuarioDAO
from .dao.paciente import PacienteDAO
from .dao.medico import MedicoDAO
from .dao.secretario import SecretarioDAO


_usuario_dao = UsuarioDAO()
_paciente_dao = PacienteDAO()
_medico_dao = MedicoDAO()
_secretario_dao = SecretarioDAO()

def login(email, senha):

    cpf = _usuario_dao.verify_credentials(email, senha)
    if cpf:
        return _profiles(cpf)
    return None


def _profiles(cpf):

    profiles = { 'cpf': cpf }

    medico = _medico_dao.get_medico_from_cpf(cpf)
    if medico:
        profiles['crm'] = medico.crm
        profiles['medico'] = True

    paciente = _paciente_dao.get_paciente(cpf)
    if paciente:
        profiles['paciente'] = True

    secretario = _secretario_dao.get_secretario(cpf)
    if secretario:
        profiles['secretario'] = True

    return profiles
