import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


def main():
    schema = avro.schema.parse(open("GraphSchema.avsc", "rb").read())
    writer = DataFileWriter(open("Graphs.avro", "ab"), DatumWriter(), schema)
    writer.append(
        {
            "name": "Straight Line 2",
            "x_axis": {
                "denotes": "x",
                "units": "",
                "scale": 1.0
            },
            "y_axis": {
                "denotes": "y",
                "units": "",
                "scale": 1.0
            },
            "points":[
                {"x": 1.0, "y": 1.0}, {"x": 2.0, "y": 3.0}
            ]
        })
    writer.close()

def read():
    reader = DataFileReader(open("Graphs.avro", "rb"), DatumReader())
    for user in reader:
        print(user)
    reader.close()


if __name__ == '__main__':
    main()
    read()