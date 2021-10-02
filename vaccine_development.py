class Immunization:
    vaccineList = [[],[]] # list containing distinct vaccines and their associations with strains
    strains = [[],[]] # strains and their associations to vaccines
    
    def constructMatrix(self, lines):
        for line in lines:
            line = line.strip()
            inputs = line.split("/")
            inputs = [s.strip() for s in inputs]
            strain = inputs[0]
            vaccines = set(inputs[1:])
            self.addToVaccineList(vaccines)
            self.addToStrains(strain, vaccines)
        self.updateVaccineAssociations()
                
    def addToStrains(self, strain, vaccines):
        self.strains[0].append(strain)
        self.strains[1].append(vaccines)

    def addToVaccineList(self, vaccines):
        for vac in vaccines:
            idx = self.vaccineList[0].index(vac) if vac in self.vaccineList[0] else -1
            if idx == -1:
                self.vaccineList[0].append(vac)
                
    def updateVaccineAssociations(self):
        for idx in range(len(self.vaccineList[0])):
            self.vaccineList[1].append([]) # initialize vaccine to strain mappings
        
        for idx in range(len(self.strains[0])):
            strain = self.strains[0][idx]
            for vac in self.strains[1][idx]:
                strainListIdx = self.vaccineList[0].index(vac)
                self.vaccineList[1][strainListIdx].append(strain) # update all mapped vaccines in vaccinelist with the strain

        for idx in range(len(self.vaccineList[0])):
            print("Idx is" + str(idx))
            print("Strain List for :: " + self.vaccineList[0][idx] + " >> " + str(self.vaccineList[1][idx]))

    def readInputFile(self, inputFile):
        with open(inputFile, 'r') as f:
            lines = f.readlines()
            self.constructMatrix(lines)
    
    def displayAll(self):
        output = "--------Function displayAll--------\n"
        output += "Total no. of strains:" + str(len(self.strains[0])) + "\n"
        output += "Total no. of vaccines:" + str(len(self.vaccineList[0])) + "\n"
        output += "List of strains:\n"
        for strain in self.strains[0]:
            output += strain + "\n"
        output += "\n"
        output += "List of vaccines:\n"
        for vaccine in self.vaccineList[0]:
            output += vaccine + "\n"
        output += "-----------------------------------------\n"
        return output

    def displayStrains(self, vaccine):
        output = "--------Function displayStrain --------\n" + "Vaccine name:"+ vaccine + "\n"
        foundStrains = []
        if vaccine in self.vaccineList[0]:
            foundStrains = self.vaccineList[1][self.vaccineList[0].index(vaccine)]
            output += "List of Strains:\n"
            for s in foundStrains:
                output += s+"\n"
        else:
            output += "No strain(s) found for the vaccine\n"
        output += "-----------------------------------------\n"
        return output

    def displayVaccine(self, strain): 
        output = "--------Function displayVaccine --------\n Strain name: " +strain+ "\n"        
        if strain in self.strains[0]:
            vaccines = self.strains[1][self.strains[0].index(strain)]
            output += "List of Vaccines:\n"
            for v in vaccines:
                output += v + "\n"
        else:
            output += "No vaccine(s) found for the strain\n"
        output += "-----------------------------------------\n"
        return output
    
    def commonStrain(self,  vacA,  vacB):
        output = "--------Function commonStrain --------\n"
        output += "Vaccine A: " + vacA + "\n" + "Vaccine B: " + vacB + "\n"
        # Get the strain list for source vaccine
        strainQueue = self.vaccineList[1][self.vaccineList[0].index(vacA)].copy()
        commonStrain = None
        while strainQueue:
            strain = strainQueue.pop(0)
            if vacB in self.strains[1][self.strains[0].index(strain)]:
                commonStrain = strain
                break
        if commonStrain is not None:
            output += "common strain: Yes," + commonStrain + "\n"
        else:
            output += "common strain: No common strain found \n"
        output += "-----------------------------------------\n"
        return output
            

    def findVaccineConnect(self, vacA, vacB):
        output = "--------Function findVaccineConnect --------\n"
        output += "Vaccine A: " + vacA + "\n" + "Vaccine B: " + vacB + "\n"
        # Get the strain list for source vaccine
        idx = self.vaccineList[0].index(vacA)
        strainStack = self.vaccineList[1][idx].copy()
        strainsVisited = []
        
        vaccineStack = []
        vaccinesVisited = [vacA]

        # add validation conditions
        vaccineConnectPath = [vacA]
        while strainStack:
            strain = strainStack.pop()
            if strain not in strainsVisited:
                strainsVisited.append(strain)
                vaccineConnectPath.append(strain)

            strainIdx = self.strains[0].index(strain)
            for v in self.strains[1][strainIdx]:
                    if v not in vaccinesVisited:
                        vaccineStack.append(v) # add vaccine to the stack only if not visited yet            

            # base condition to terminate path 
            if vacB in self.strains[1][self.strains[0].index(strain)]:
                vaccineConnectPath.append(vacB)
                break
            else:
                currVac = vaccineStack.pop()
                
                if currVac not in vaccinesVisited:
                    vaccinesVisited.append(currVac)
                    vaccineConnectPath.append(currVac)

                vacIdx = self.vaccineList[0].index(currVac)
                for s in self.vaccineList[1][vacIdx]:
                    if s not in strainsVisited:
                        strainStack.append(s) # add strain to the stack only if not visited yet
        

        if vaccineConnectPath[-1] == vacB:
            output += "Related: Yes, " + " > ".join(vaccineConnectPath)
        else:
            output += "Related: No relation found"
        return output
        


def writeToOutput(output):
    with open("outputPS16.txt", "a+") as f:
        f.write(output)


def main():
    immunize = Immunization()
    immunize.readInputFile('inputPS16.txt')
    output = immunize.displayAll()
    with open("promptsPS16.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            action_n_name = [s.strip() for s in l.split(":")]
            if action_n_name[0] == "findStrain":
                output += immunize.displayStrains(action_n_name[1])
            if action_n_name[0] == "listVaccine":            
                output += immunize.displayVaccine(action_n_name[1])
            if action_n_name[0] == "commonStrain":
                output += immunize.commonStrain(action_n_name[1], action_n_name[2])
            if action_n_name[0] == "vaccineConnect":
                output += immunize.findVaccineConnect(action_n_name[1], action_n_name[2])
    print(output)
    writeToOutput(output=output)


if __name__ == "__main__":
    main()
