class RemoveProfessorIdFromCourses < ActiveRecord::Migration[7.1]
  def change
    remove_column :courses, :professor_id, :integer
  end
end
