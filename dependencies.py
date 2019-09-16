from config import Config
from domain.answer.answer_repository import AnswerRepository
from domain.answer.answer_service import AnswerService
from domain.choice.choice_repository import ChoiceRepository
from domain.question.question_repository import QuestionRepository
from domain.question.question_service import QuestionService
from domain.user.role import Role
from domain.user.user import User
from domain.user.user_repository import UserRepository
from domain.user.user_service import UserService

question_repository = QuestionRepository(Config)
choice_repository = ChoiceRepository(Config)
answer_repository = AnswerRepository(Config)
user_repository = UserRepository(Config)
question_service = QuestionService(question_repository, choice_repository)
answer_service = AnswerService(answer_repository)
user_service = UserService(user_repository)

admin_user = User(None,
                  'Administrator',
                  Config.DEFAULT_ADMIN_USER,
                  Role.ADMIN,
                  Config.DEFAULT_ADMIN_PASSWORD,
                  None,
                  None)
user_service.create(admin_user)
