class BankersAlgorithm:
    def __init__(self, allocation, max_demand, available):
        self.allocation = allocation  # Allocation matrix
        self.max_demand = max_demand  # Maximum demand matrix
        self.available = available  # Available resources vector
        self.processes = len(allocation)  # Number of processes
        self.resources = len(available)  # Number of resources

        self.need = self.calculate_need()  # Need matrix
        self.safe_sequence = []  # Safe sequence

    def calculate_need(self):
        need = []
        for i in range(self.processes):
            row = []
            for j in range(self.resources):
                row.append(self.max_demand[i][j] - self.allocation[i][j])
            need.append(row)
        return need

    def is_safe(self, process, work, finish):
        for j in range(self.resources):
            if self.need[process][j] > work[j]:
                return False
        return True

    def run(self):
        work = self.available.copy()
        finish = [False] * self.processes
        safe_sequence = []

        while True:
            found = False
            for i in range(self.processes):
                if not finish[i] and self.is_safe(i, work, finish):
                    # Process can be executed
                    for j in range(self.resources):
                        work[j] += self.allocation[i][j]

                    finish[i] = True
                    safe_sequence.append(i)
                    found = True

            if not found:
                break

        if len(safe_sequence) == self.processes:
            self.safe_sequence = safe_sequence
            return True
        else:
            return False


# Test the Banker's algorithm
if __name__ == "__main__":
    # Example matrices
    allocation_matrix = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    max_demand_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    available_resources = [3, 3, 2]

    # Create BankersAlgorithm object
    banker = BankersAlgorithm(allocation_matrix, max_demand_matrix, available_resources)

    # Run the Banker's algorithm
    if banker.run():
        print("System is in a safe state.")
        print("Safe sequence:", banker.safe_sequence)
    else:
        print("System is in an unsafe state.")

