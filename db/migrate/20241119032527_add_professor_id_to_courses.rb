class AddProfessorIdToCourses < ActiveRecord::Migration[7.1]
  def change
    add_column :courses, :professor_id, :integer
  end
end
