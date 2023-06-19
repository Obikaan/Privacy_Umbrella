import threading


import pandas as pd

from threading import Thread

class Anonymize:

    def load_original_df(self):

        # Load the original dataset
        self.df = pd.read_csv('heart.csv')
        return self.df

    def get_euqivalence_classes(self, df, quasi_identifiers_n):
        # Group the data based on quasi-identifiers
        groups = df.groupby(quasi_identifiers_n)
        return groups


    def load_anonymized_df(self):
        # Loads the anonymized dataset
        self.anonymized_df = pd.read_csv('anonymized_heart.csv')
        return self.anonymized_df






def leadersending(equiv_class,curr_grp):
    # Leader of current group sending Data to the data collector

    if curr_grp not in already_done:
        already_done.append(curr_grp)
        try:
            available_data_for_collector.append(equiv_class.get_group(curr_grp).head())
        except:
            # try catch needed since dataset gave me NAN as input
            print("")










def datacollector(equiv_class):
    # Data collector requesting information for all given Groups
    # and Starting a thread that is used as the "leader" of a data holding group
    for i in equiv_class.groups.keys():
        tmp_thread = Thread(target= leadersending(equiv_class, i))








def time_until_adversarys_success():
    # Simulates the communication between a leader of an equivalence class and a data collector

    quasi_identifiers = ["age_range", "chol_range", "sex"]


    anonymize = Anonymize()

    og_dataset = anonymize.load_original_df()
    ano_dataset = anonymize.load_anonymized_df()
    equivalence_classes_anom = anonymize.get_euqivalence_classes(ano_dataset, quasi_identifiers)
    k_anonymity_level = equivalence_classes_anom.size().min()

    if k_anonymity_level == 1:
        print("The Adversary can detect the sender immediately because the anonymity level is equal to 1 ")

    else:
        check = threading.Condition()
        keys_anom = equivalence_classes_anom.groups.keys()

        datacollector_ = Thread(target = datacollector(equivalence_classes_anom))

        datacollector_.start()











    return available_data_for_collector
already_done = []
available_data_for_collector = []
x = time_until_adversarys_success()

