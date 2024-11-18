class CreateJoinTableCoursesProfessors < ActiveRecord::Migration[7.1]
  def change
    create_join_table :courses, :professors do |t|
      # t.index [:course_id, :professor_id]
      # t.index [:professor_id, :course_id]
    end
  end
end
