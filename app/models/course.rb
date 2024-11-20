class Course < ApplicationRecord
    validates_presence_of :name, :code

    has_and_belongs_to_many :professors
end
