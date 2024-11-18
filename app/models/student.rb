class Student < ApplicationRecord
    validates :username, presence: true, uniqueness: true
    validates :password, presence: true
    has_many :reviews
    has_many :comments
end
