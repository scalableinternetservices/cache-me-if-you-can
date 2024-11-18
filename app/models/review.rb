class Review < ApplicationRecord
  belongs_to :student
  belongs_to :professor
  has_many :comments
end
