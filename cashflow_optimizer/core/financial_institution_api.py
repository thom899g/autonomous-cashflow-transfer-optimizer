from abc import ABC, abstractmethod
import logging

class FinancialInstitutionAPI(ABC):
    """Abstract base class for financial institution APIs.
    
    This class defines the interface for interacting with different banks' APIs.
    Subclasses should implement methods to fetch and update account data.
    
    Why this choice: Using an abstract class enforces a uniform API across institutions,
    making the system more modular and easier to extend.
    """
    
    @abstractmethod
    def get_account_data(self, account_id):
        """Fetches detailed account information."""
        pass
    
    @abstractmethod
    def transfer_funds(self, from_id, to_id, amount):
        """Initiates a fund transfer between accounts."""
        pass

class BankAdapter(FinancialInstitutionAPI):
    """Adapter for a specific bank's API.
    
    Implements the abstract interface for a particular bank, handling data transformation and API calls.
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def get_account_data(self, account_id):
        try:
            # Implement API call to fetch data
            return {"balance": 1000.0, "transactions": []}
        except Exception as e:
            self.logger.error(f"Failed to fetch data: {e}")
            raise
    
    def transfer_funds(self, from_id, to_id, amount):
        try:
            # Implement API call for transfer
            return True
        except Exception as e:
            self.logger.error(f"Transfer failed: {e}")
            raise