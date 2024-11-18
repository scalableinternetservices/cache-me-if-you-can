class Review < ApplicationRecord
  belongs_to :student
  belongs_to :professor
  has_many :comments

  validates :content, presence: true
  validates :rating, presence: true, inclusion: { in: 1..5 }
end
