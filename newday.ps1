[CmdletBinding(SupportsShouldProcess=$True)]
Param(
    [Parameter(Position=0, mandatory=$True)]
    [int]$day
)

$dir="$Home\Code\aoc-2020"
$new_dir = $dir + "\Day" + $day

New-Item -Path $new_dir -ItemType "directory"

Set-Location $new_dir

New-Item -Path "Part1.py" -ItemType "file"
New-Item -Path "Part2.py" -ItemType "file"
New-Item -Path "input.txt" -ItemType "file"

Set-Location ".."