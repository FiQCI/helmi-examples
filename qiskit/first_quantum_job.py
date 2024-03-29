import os

from iqm.qiskit_iqm import IQMProvider

from qiskit import QuantumCircuit, QuantumRegister, execute

shots = 1000

qreg = QuantumRegister(2, "QB")
circuit = QuantumCircuit(qreg, name='Bell pair circuit')

circuit.h(qreg[0])
circuit.cx(qreg[0], qreg[1])
circuit.measure_all()

# Uncomment if you wish to print the circuit
# print(circuit.draw())

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
if not HELMI_CORTEX_URL:
    raise ValueError("Environment variable HELMI_CORTEX_URL is not set")

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

# Retrieving backend information
# print(f'Native operations: {backend.operation_names}')
# print(f'Number of qubits: {backend.num_qubits}')
# print(f'Coupling map: {backend.coupling_map}')

job = execute(circuit, backend, shots=shots)
result = job.result()
exp_result = job.result()._get_experiment(circuit)
# You can retrieve the job at a later date with backend.retrieve_job(job_id)
# Uncomment the following lines to get more information about your submitted job
print("Job ID: ", job.job_id())
# print(result.request.circuits)
print("Calibration Set ID: ", exp_result.calibration_set_id)
# print(result.request.qubit_mapping)
# print(result.request.shots)

counts = result.get_counts()
print(counts)
