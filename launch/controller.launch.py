from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration



def generate_launch_description():
    
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="True",
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    diff_drive = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["g_bot_controller", 
                   "--controller-manager", 
                   "/controller_manager"
        ]
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            joint_state_broadcaster_spawner,
            diff_drive
        ]
    )