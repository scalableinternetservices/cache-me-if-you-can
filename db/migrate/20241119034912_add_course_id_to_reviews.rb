class AddCourseIdToReviews < ActiveRecord::Migration[7.1]
  def change
    add_column :reviews, :course_id, :integer
  end
end
