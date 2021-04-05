from datetime import date

from train_management.models import DayPlanning, DvzoFunction, Train, TrainConfiguration, Vehicle


class SetupHelper:
    def __init__(self):
        self.elisabeth_lok = None
        self.peter_waggon = None
        self.emma_waggon = None
        self.lisa_waggon = None
        self.BC4563 = None
        self.C6109 = None
        self.WR109 = None
        self.F202 = None
        self.Bw_Neuthal = None
        self.Bw_Baeretswil = None
        self.Kobe_Baeretswil = None
        self.Sw_Baeretswil = None
        self.V_Hinwil = None
        self.Hzf = None
        self.Hzm = None
        self.Hzs = None
        self.K = None
        self.Lf = None
        self.Z = None
        self.Sw_Bauma = None
        self.Wr = None
        self.RoWa_Bauma = None

    @staticmethod
    def get_day_planning(date_str="2021-02-13", label="Default label dayplanning"):
        day_planning = DayPlanning(
            label=label,
            day_planning_type=DayPlanning.DayPlanningType.EXTRA,
            date=date.fromisoformat(date_str),
            status=DayPlanning.DayPlanningStatus.CONFIRMED,
            paid=True,
        )
        day_planning.save()
        return day_planning

    @staticmethod
    def get_train(day_planning):
        train = Train(
            label="Thomas the Train",
            km=400,
            day_planning=day_planning,
        )
        train.save()
        return train

    def create_train_config(self, train):
        config1 = TrainConfiguration(
            vehicle=self.elisabeth_lok,
            train=train,
            sorting=0,
        )
        config1.save()
        config2 = TrainConfiguration(
            vehicle=self.lisa_waggon,
            train=train,
            sorting=1,
        )
        config2.save()
        config3 = TrainConfiguration(
            vehicle=self.peter_waggon,
            train=train,
            sorting=2,
        )
        config3.save()
        config4 = TrainConfiguration(
            vehicle=self.emma_waggon,
            train=train,
            sorting=3,
        )
        config4.save()

    def create_train_components(self):
        self.emma_waggon = Vehicle(
            label="Wagen Emma",
            historic_name="Emma the waggon",
            description="Emma is a very nice waggon.",
            uic="91 85 4927 43 1",
            gross_weight=1001.7,
            seats=23,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1990,
            last_revision=date.fromisoformat("1999-05-23"),
            next_revision=date.fromisoformat("2100-04-11"),
            axles_distance=40000.88,
            length=40.1,
            manufacturer="Stadler Rail",
            max_speed=99,
        )
        self.emma_waggon.save()

        self.lisa_waggon = Vehicle(
            label="Wagen Lisa",
            historic_name="Lisa the waggon",
            description="Lisa is a very nice waggon.",
            uic="91 85 4927 43 1",
            gross_weight=1001.7,
            seats=23,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1990,
            last_revision=date.fromisoformat("1999-05-23"),
            next_revision=date.fromisoformat("2100-04-11"),
            axles_distance=40000.88,
            length=40.1,
            manufacturer="Stadler Rail",
            max_speed=99,
        )
        self.lisa_waggon.save()

        self.peter_waggon = Vehicle(
            label="Wagen Peter",
            historic_name="Peter the waggon",
            description="Peter is a very nice waggon.",
            uic="91 85 4927 43 1",
            gross_weight=1001.7,
            seats=23,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1990,
            last_revision=date.fromisoformat("1999-05-23"),
            next_revision=date.fromisoformat("2100-04-11"),
            axles_distance=40000.88,
            length=40.1,
            manufacturer="Stadler Rail",
            max_speed=99,
        )
        self.peter_waggon.save()

        self.elisabeth_lok = Vehicle(
            label="Loki Elisabeth",
            historic_name="Elisabeth the Lok",
            description="The red happy fat Elisabeth.",
            uic="91 85 4927 43 1",
            gross_weight=1001.7,
            seats=23,
            vehicle_type=Vehicle.VehicleType.ENGINE,
            status=Vehicle.Status.AVAILABLE,
            home=Vehicle.Home.BAUMA,
            start_year=1990,
            last_revision=date.fromisoformat("1999-05-23"),
            next_revision=date.fromisoformat("2100-04-11"),
            axles_distance=40000.88,
            length=40.1,
            manufacturer="Stadler Rail",
            traction_25=44,
            traction_30=30,
            power_unit=Vehicle.PowerUnit.STEAM,
            steam_heating=Vehicle.SteamHeating.FRONT,
            max_speed=500,
        )
        self.elisabeth_lok.save()

        self.BC4563 = Vehicle(
            label="BC4563",
            historic_name="BC4563",
            description="Grüner Wagen mit 2. und 3. Klasse",
            uic="55 85 2429 101-7",
            gross_weight=15,
            seats=45,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1886,
            last_revision=date.fromisoformat("2018-10-24"),
            next_revision=date.fromisoformat("2026-10-24"),
            axles_distance=5,
            length=12.07,
            manufacturer="SIG",
            max_speed=60,
        )
        self.BC4563.save()

        self.C6109 = Vehicle(
            label="C6109",
            historic_name="C6109",
            description="Grüner Wagen mit 3. Klasse",
            uic="55 85 2803 102-1",
            gross_weight=20,
            seats=60,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1913,
            last_revision=date.fromisoformat("2014-02-13"),
            next_revision=date.fromisoformat("2022-02-13"),
            axles_distance=9.2,
            length=14.6,
            manufacturer="SWS",
            max_speed=60,
        )
        self.C6109.save()

        self.WR109 = Vehicle(
            label="WR109",
            historic_name="WR109",
            description="Waggon Restaurant",
            uic="55 85 8803 109-3",
            gross_weight=19,
            seats=40,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.SEAT,
            home=Vehicle.Home.BAUMA,
            start_year=1912,
            last_revision=date.fromisoformat("2019-05-04"),
            next_revision=date.fromisoformat("2027-05-04"),
            axles_distance=8,
            length=13.29,
            manufacturer="SIG",
            max_speed=60,
        )
        self.WR109.save()

        self.F202 = Vehicle(
            label="F202",
            historic_name="F405",
            description="Gepäckwagen",
            uic="55 85 9603 202-6",
            gross_weight=19,
            vehicle_type=Vehicle.VehicleType.CARRIAGE,
            status=Vehicle.Status.AVAILABLE,
            carriage_type=Vehicle.CarriageType.LUGGAGE,
            home=Vehicle.Home.BAUMA,
            start_year=1891,
            last_revision=date.fromisoformat("2015-11-01"),
            next_revision=date.fromisoformat("2023-11-01"),
            axles_distance=4,
            length=8.64,
            manufacturer="SIG",
            max_speed=40,
        )
        self.F202.save()

    def create_function(self):
        self.Bw_Neuthal = DvzoFunction(
            label="Barrierenwärter",
            label_short="Bw",
            sorting="10",
            function_type=DvzoFunction.FunctionType.NEUTHAL,
        )
        self.Bw_Neuthal.save()

        self.Bw_Baeretswil = DvzoFunction(
            label="Barrierenwärter",
            label_short="Bw",
            sorting="30",
            function_type=DvzoFunction.FunctionType.BAERETSWIL,
        )
        self.Bw_Baeretswil.save()

        self.Kobe_Baeretswil = DvzoFunction(
            label="Koordinator",
            label_short="KoBe",
            sorting="10",
            function_type=DvzoFunction.FunctionType.BAERETSWIL,
        )
        self.Kobe_Baeretswil.save()

        self.Sw_Baeretswil = DvzoFunction(
            label="Stationswärter",
            label_short="Sw",
            sorting="20",
            function_type=DvzoFunction.FunctionType.BAERETSWIL,
        )
        self.Sw_Baeretswil.save()

        self.V_Hinwil = DvzoFunction(
            label="Verkauf",
            label_short="V",
            sorting="10",
            function_type=DvzoFunction.FunctionType.HINWIL,
        )
        self.V_Hinwil.save()

        self.Hzf = DvzoFunction(
            label="Heizer früh",
            label_short="Hz f",
            sorting="20",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Hzf.save()

        self.Hzm = DvzoFunction(
            label="Heizer mittel",
            label_short="Hz m",
            sorting="30",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Hzm.save()

        self.Hzs = DvzoFunction(
            label="Heizer spät",
            label_short="Hz s",
            sorting="40",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Hzs.save()

        self.K = DvzoFunction(
            label="Kondukteuer",
            label_short="K",
            sorting="120",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.K.save()

        self.Lf = DvzoFunction(
            label="Lokführer",
            label_short="Lf",
            sorting="10",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Lf.save()

        self.Z = DvzoFunction(
            label="Zugchef",
            label_short="Z",
            sorting="110",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Z.save()

        self.Sw_Bauma = DvzoFunction(
            label="Stationswärter",
            label_short="Sw",
            sorting="10",
            function_type=DvzoFunction.FunctionType.BAUMA,
        )
        self.Sw_Bauma.save()

        self.Wr = DvzoFunction(
            label="Gastro",
            label_short="WR",
            sorting="210",
            function_type=DvzoFunction.FunctionType.TRAIN,
        )
        self.Wr.save()

        self.RoWa_Bauma = DvzoFunction(
            label="Rottenwagen",
            label_short="RoWa",
            sorting="110",
            function_type=DvzoFunction.FunctionType.BAUMA,
        )
        self.RoWa_Bauma.save()
