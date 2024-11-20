class CreateProfessors < ActiveRecord::Migration[7.1]
  def change
    create_table :professors do |t|
      t.string :name
      t.string :department
      t.string :university  # Added the university field here

      t.timestamps
    end
  end
end
