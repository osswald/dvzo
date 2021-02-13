from train_management.models import DayPlanning
from train_management.models import Train
from train_management.models import Vehicle
from train_management.models import TrainConfiguration
from datetime import date


class SetupHelper:
    def __init__(self):
        self.elisabeth_lok = None
        self.peter_waggon = None
        self.emma_waggon = None
        self.lisa_waggon = None

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
