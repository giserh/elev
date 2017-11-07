# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# model_buffer_clip_all.py
# Created on: 2015-05-26 21:20:24.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: model_buffer_clip_all <Area_of_Interest> <Out_Root_Workspace> <Out_Folder_Name> <Distance> <Map_to_clip_from> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("D:/p/ytdemv3/Toolbox.tbx")

# Script arguments
Area_of_Interest = arcpy.GetParameterAsText(0)
if Area_of_Interest == '#' or not Area_of_Interest:
    Area_of_Interest = "nts_250k_index" # provide a default value if unspecified

Out_Root_Workspace = arcpy.GetParameterAsText(1)
if Out_Root_Workspace == '#' or not Out_Root_Workspace:
    Out_Root_Workspace = "D:\\p\\ytdemv3" # provide a default value if unspecified

Out_Folder_Name = arcpy.GetParameterAsText(2)
if Out_Folder_Name == '#' or not Out_Folder_Name:
    Out_Folder_Name = "Work_%NTS" # provide a default value if unspecified

Distance = arcpy.GetParameterAsText(3)
if Distance == '#' or not Distance:
    Distance = "3000 Meters" # provide a default value if unspecified

Map_to_clip_from = arcpy.GetParameterAsText(4)

# Local variables:
Workspace = Out_Root_Workspace
Clipped_gdb = Workspace
selection_buffer__distance_num_m = Clipped_gdb

# Process: Distance_to_number
arcpy.CalculateValue_management("\"%Distance%\".split()[0]", "", "Variant")

# Process: Create Folder
arcpy.CreateFolder_management(Out_Root_Workspace, Out_Folder_Name)

# Process: Create FileGDB
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment4 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\mhwilkie\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment5 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment6 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment7 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment8 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment9 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment10 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment11 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment12 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment13 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment14 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment15 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment16 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment17 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment18 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = "PROJCS['NAD_1983_CSRS_Yukon_Albers',GEOGCS['GCS_North_American_1983_CSRS',DATUM['D_North_American_1983_CSRS',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',500000.0],PARAMETER['Central_Meridian',-132.5],PARAMETER['Standard_Parallel_1',61.66666666666666],PARAMETER['Standard_Parallel_2',68.0],PARAMETER['Latitude_Of_Origin',59.0],UNIT['Meter',1.0]],VERTCS['CGVD_1928',VDATUM['Canadian_Geodetic_Vertical_Datum_of_1928'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]]"
tempEnvironment19 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment20 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment21 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment22 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment23 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment24 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment25 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment26 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment27 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment28 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment29 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment30 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment31 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment32 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment33 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment34 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment35 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = "NAD_1927_To_NAD_1983_NADCON"
tempEnvironment36 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment37 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment38 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment39 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment40 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment41 = arcpy.env.workspace
arcpy.env.workspace = "C:\\Users\\mhwilkie\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment42 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment43 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment44 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.gp.toolbox = "D:/p/ytdemv3/Toolbox.tbx";
# Warning: the toolbox D:/p/ytdemv3/Toolbox.tbx DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.CreateFileGDB(...) with arcpy.CreateFileGDB_ALIAS(...)
arcpy.gp.CreateFileGDB(Workspace, "clipped", "CURRENT")
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.XYDomain = tempEnvironment3
arcpy.env.scratchWorkspace = tempEnvironment4
arcpy.env.cartographicPartitions = tempEnvironment5
arcpy.env.terrainMemoryUsage = tempEnvironment6
arcpy.env.MTolerance = tempEnvironment7
arcpy.env.compression = tempEnvironment8
arcpy.env.coincidentPoints = tempEnvironment9
arcpy.env.randomGenerator = tempEnvironment10
arcpy.env.outputCoordinateSystem = tempEnvironment11
arcpy.env.rasterStatistics = tempEnvironment12
arcpy.env.ZDomain = tempEnvironment13
arcpy.env.transferDomains = tempEnvironment14
arcpy.env.resamplingMethod = tempEnvironment15
arcpy.env.snapRaster = tempEnvironment16
arcpy.env.projectCompare = tempEnvironment17
arcpy.env.cartographicCoordinateSystem = tempEnvironment18
arcpy.env.configKeyword = tempEnvironment19
arcpy.env.outputZFlag = tempEnvironment20
arcpy.env.qualifiedFieldNames = tempEnvironment21
arcpy.env.tileSize = tempEnvironment22
arcpy.env.parallelProcessingFactor = tempEnvironment23
arcpy.env.pyramid = tempEnvironment24
arcpy.env.referenceScale = tempEnvironment25
arcpy.env.extent = tempEnvironment26
arcpy.env.XYTolerance = tempEnvironment27
arcpy.env.tinSaveVersion = tempEnvironment28
arcpy.env.nodata = tempEnvironment29
arcpy.env.MDomain = tempEnvironment30
arcpy.env.spatialGrid1 = tempEnvironment31
arcpy.env.cellSize = tempEnvironment32
arcpy.env.outputZValue = tempEnvironment33
arcpy.env.outputMFlag = tempEnvironment34
arcpy.env.geographicTransformations = tempEnvironment35
arcpy.env.spatialGrid2 = tempEnvironment36
arcpy.env.ZResolution = tempEnvironment37
arcpy.env.mask = tempEnvironment38
arcpy.env.spatialGrid3 = tempEnvironment39
arcpy.env.maintainSpatialIndex = tempEnvironment40
arcpy.env.workspace = tempEnvironment41
arcpy.env.MResolution = tempEnvironment42
arcpy.env.derivedPrecision = tempEnvironment43
arcpy.env.ZTolerance = tempEnvironment44

# Process: Buffer
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment4 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\mhwilkie\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment5 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment6 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment7 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment8 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment9 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment10 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment11 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment12 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment13 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment14 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment15 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment16 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment17 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment18 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = "PROJCS['NAD_1983_CSRS_Yukon_Albers',GEOGCS['GCS_North_American_1983_CSRS',DATUM['D_North_American_1983_CSRS',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',500000.0],PARAMETER['Central_Meridian',-132.5],PARAMETER['Standard_Parallel_1',61.66666666666666],PARAMETER['Standard_Parallel_2',68.0],PARAMETER['Latitude_Of_Origin',59.0],UNIT['Meter',1.0]],VERTCS['CGVD_1928',VDATUM['Canadian_Geodetic_Vertical_Datum_of_1928'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]]"
tempEnvironment19 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment20 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment21 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment22 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment23 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment24 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment25 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment26 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment27 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment28 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment29 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment30 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment31 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment32 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment33 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment34 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment35 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = "NAD_1927_To_NAD_1983_NADCON"
tempEnvironment36 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment37 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment38 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment39 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment40 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment41 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment42 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment43 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.Buffer_analysis(Area_of_Interest, selection_buffer__distance_num_m, Distance, "FULL", "ROUND", "LIST", "TILE_NAME", "PLANAR")
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.XYDomain = tempEnvironment3
arcpy.env.scratchWorkspace = tempEnvironment4
arcpy.env.cartographicPartitions = tempEnvironment5
arcpy.env.terrainMemoryUsage = tempEnvironment6
arcpy.env.MTolerance = tempEnvironment7
arcpy.env.compression = tempEnvironment8
arcpy.env.coincidentPoints = tempEnvironment9
arcpy.env.randomGenerator = tempEnvironment10
arcpy.env.outputCoordinateSystem = tempEnvironment11
arcpy.env.rasterStatistics = tempEnvironment12
arcpy.env.ZDomain = tempEnvironment13
arcpy.env.transferDomains = tempEnvironment14
arcpy.env.resamplingMethod = tempEnvironment15
arcpy.env.snapRaster = tempEnvironment16
arcpy.env.projectCompare = tempEnvironment17
arcpy.env.cartographicCoordinateSystem = tempEnvironment18
arcpy.env.configKeyword = tempEnvironment19
arcpy.env.outputZFlag = tempEnvironment20
arcpy.env.qualifiedFieldNames = tempEnvironment21
arcpy.env.tileSize = tempEnvironment22
arcpy.env.parallelProcessingFactor = tempEnvironment23
arcpy.env.pyramid = tempEnvironment24
arcpy.env.referenceScale = tempEnvironment25
arcpy.env.extent = tempEnvironment26
arcpy.env.XYTolerance = tempEnvironment27
arcpy.env.tinSaveVersion = tempEnvironment28
arcpy.env.nodata = tempEnvironment29
arcpy.env.MDomain = tempEnvironment30
arcpy.env.spatialGrid1 = tempEnvironment31
arcpy.env.cellSize = tempEnvironment32
arcpy.env.outputZValue = tempEnvironment33
arcpy.env.outputMFlag = tempEnvironment34
arcpy.env.geographicTransformations = tempEnvironment35
arcpy.env.spatialGrid2 = tempEnvironment36
arcpy.env.ZResolution = tempEnvironment37
arcpy.env.mask = tempEnvironment38
arcpy.env.spatialGrid3 = tempEnvironment39
arcpy.env.maintainSpatialIndex = tempEnvironment40
arcpy.env.MResolution = tempEnvironment41
arcpy.env.derivedPrecision = tempEnvironment42
arcpy.env.ZTolerance = tempEnvironment43

# Process: 1 - Clip All Layers
arcpy.gp.toolbox = "D:/p/ytdemv3/Toolbox.tbx";
# Warning: the toolbox D:/p/ytdemv3/Toolbox.tbx DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.clipAllLayers(...) with arcpy.clipAllLayers_ALIAS(...)
arcpy.gp.clipAllLayers(Map_to_clip_from, selection_buffer__distance_num_m, Clipped_gdb)

