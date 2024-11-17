class Student < ApplicationRecord
    validates :username, presence: true, uniqueness: true
    validates :password, presence: true
end
