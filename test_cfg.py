import FWCore.ParameterSet.Config as cms



process = cms.Process("unpack")
process.load('HGCal.RawToDigi.hgcaltbdigis_cfi')
process.load('HGCal.Reco.hgcalrechitproducer_cfi')

process.source = cms.Source("HGCalTBTextSource",
                            run=cms.untracked.int32(2), ### maybe this should be read from the file
                            fileNames=cms.untracked.vstring("file:SKIROC_RO.txt") ### here a vector is provided, but in the .cc only the first one is used TO BE FIXED

)

process.dumpRaw = cms.EDAnalyzer("DumpFEDRawDataProduct",
                              dumpPayload=cms.untracked.bool(True))

process.dumpDigi = cms.EDAnalyzer("HGCalDigiDump")

process.output = cms.OutputModule("PoolOutputModule",
                                  compressionAlgorithm = cms.untracked.string('LZMA'),
                                  compressionLevel = cms.untracked.int32(4),
                                  dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER'),
        filterName = cms.untracked.string('')
        ),
                                  #dropMetaData = cms.untracked.string('ALL'),
                                  eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
                                 fastCloning = cms.untracked.bool(False),
                                 fileName = cms.untracked.string('test_output.root'), #options.output),
#                                 outputCommands = process.MICROAODSIMEventContent.outputCommands,
#                                 overrideInputFileSplitLevels = cms.untracked.bool(True),
#                                 SelectEvents = SelectEventsPSet
                                 )

process.p =cms.Path(process.dumpRaw*process.hgcaltbdigis*process.dumpDigi * process.hgcaltbrechits)
process.end = cms.EndPath(process.output)
