from sdjlfdk import app
from sdjlfdk.app import Base_URL


class GetApi:
    def get_login(self,session,mobile,password):
        mydata = {"mobile":mobile,"password":password}
        return session.post(Base_URL + "login",json = mydata)

    def emp_add(self,session):
        mydata = {"username":"huanhuo11","mobile":"13566688845","workNumber":"121232343654"}
        return session.post(Base_URL +"user" ,json = mydata,
                            headers = {"Authorization": "Bearer " + app.Token})

    def emp_update(self,session):
        # return session.put(Base_URL+"user/" + app.ID,json = {"username":"huanhuo11AB"},
        #                    headers ={"Authorization":"Bearer " +app.Token})

        return session.put(Base_URL+"user/" + app.ID,json = {"username":"huanhuo11AB"},
                           headers ={"Authorization":"Bearer " +app.Token})

    def emp_get(self,session):
        return session.get(Base_URL+"user/" + app.ID,
                           headers ={"Authorization":"Bearer " +app.Token})

    def emp_delete(self,session):
        return session.delete(Base_URL+"user/" + app.ID,
                           headers={"Authorization": "Bearer " + app.Token})