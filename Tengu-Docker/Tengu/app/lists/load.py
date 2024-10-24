
import os
import glob

class ASN:
    @staticmethod
    def load() -> list:
        # Get current directory
        current_dir = os.path.dirname(os.path.abspath(__file__)) 
        
        # Joined path to asn folder
        path = os.path.join(current_dir, "asns")

        txt_files = glob.glob(os.path.join(path, '*.txt'))
        
        # ASN List
        asns = []

        # Loop through .txt files containing flagged ASNs
        for txt in txt_files:
            with open(txt, 'r') as f:
                data = f.readlines()
                asns.extend([line.strip() for line in data])  # Flattening and stripping newlines
        return asns
    
class UA:
    @staticmethod
    def load() -> list:
        # Get current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Joined path to the UA folder
        path = os.path.join(current_dir, "user-agents")

        # Glob
        txt_files = glob.glob(os.path.join(path, "*.txt"))

        # UA List
        uas = []

        for txt in txt_files:
            # Open List
            with open(txt, 'r') as f:
                data = f.readlines()
                uas.extend([line.strip() for line in data])
        return uas
    
class REF:
    @staticmethod
    def load() -> list:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, "referers")
        txt_files = glob.glob(os.path.join(path, '*.txt'))
        refs = []
        for txt in txt_files:
            with open(txt, 'r') as f:
                data = f.readlines()
                refs.extend([line.strip() for line in data])
        return refs
    
class IP:
    @staticmethod
    def load() -> list:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, "ips")
        txt_files = glob.glob(os.path.join(path, '*.txt'))
        ips = []
        for txt in txt_files:
            with open(txt, 'r') as f:
                data = f.readlines()
                ips.extend([line.strip()] for line in data)
        return ips
    
if __name__ == "__main__":
    print(ASN.load())