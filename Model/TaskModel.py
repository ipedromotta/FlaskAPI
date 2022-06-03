from Controller.ResponseController import ResponseController
from Model.Entity import Entity
from Model.Enum.RequestEnum import RequestEnum


class TaskModel(Entity):
    def __init__(self, ID=None, TITLE=None, DESCRIPTION=None, COMPLETED=False):
        super(Entity, self)
        self.Id = ID
        self.Title = TITLE
        self.Description = DESCRIPTION
        self.Completed = COMPLETED

    def get_tasks(self, conn):
        try:
            query = "SELECT * FROM tasks"
            rows = self.__loadAll__(conn, query)
            obj = self.__toList__(TaskModel, rows)

            response = ResponseController().get_response(RequestEnum.OK.value, "tasks", obj, "Consulta realizada com sucesso!")
        except:
            response = ResponseController().get_response(RequestEnum.BAD_REQUEST.value, "tasks", {}, "Erro ao consultar")

        return response

    def get_task_by_id(self, conn, task_id=False, update=False):
        try:
            query = f"SELECT * FROM tasks WHERE id = {task_id}"
            row = self.__load__(conn, query)
            obj = self.__toObject__(TaskModel, row)

            response = ResponseController().get_response(RequestEnum.OK.value, "task", obj, "Consulta realizada com sucesso!")
        except:
            response = ResponseController().get_response(RequestEnum.BAD_REQUEST.value, "task", {}, "Erro ao consultar")

        if update:
            return obj

        return response

    def insert_task(self, conn, task):
        try:
            query = f"INSERT INTO tasks (title, description) VALUES ('{task['title']}', '{task['description']}')"
            self.Execute(conn, query)

            response = ResponseController().get_response(RequestEnum.CREATED.value, "task", {}, "Inserção realizada com sucesso!")
        except:
            response = ResponseController().get_response(RequestEnum.BAD_REQUEST.value, "task", {}, "Erro ao inserir")

        return response

    def update_task(self, conn, task):
        updated_task = {}
        try:
            query = f"UPDATE tasks SET title = '{task['title']}', description = '{task['description']}', completed = {task['completed']} WHERE id = {task['id']}"
            self.Execute(conn, query)

            updated_task = self.get_task_by_id(conn, task["id"],True)
            if updated_task == None:
                raise Exception

            response = ResponseController().get_response(RequestEnum.OK.value, "task", updated_task, "Atualização realizada com sucesso!")
        except:
            response = ResponseController().get_response(RequestEnum.BAD_REQUEST.value, "task", {}, "Erro ao atualizar")

        return response

    def delete_task(self, conn, task_id):
        try:
            updated_task = self.get_task_by_id(conn, task_id,True)
            if updated_task == None:
                raise Exception

            query = f"DELETE from tasks WHERE id = {task_id}"
            self.Execute(conn, query)

            response = ResponseController().get_response(RequestEnum.OK.value, "task", updated_task, "Tarefa deletada com sucesso!")
        except:
            response = ResponseController().get_response(RequestEnum.BAD_REQUEST.value, "task", {}, "Tarefa não pode ser deletada")

        return response