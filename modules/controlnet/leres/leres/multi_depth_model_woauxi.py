import torch
import torch.nn as nn

from . import network_auxi as network
from .net_tools import get_func


class RelDepthModel(nn.Module):
    def __init__(self, backbone='resnet50'):
        super(RelDepthModel, self).__init__()
        if backbone == 'resnet50':
            encoder = 'resnet50_stride32'
        elif backbone == 'resnext101':
            encoder = 'resnext101_stride32x8d'
        self.depth_model = DepthModel(encoder)

    def inference(self, rgb):
        with torch.no_grad():
            input = rgb.to(self.depth_model.device)
            return self.depth_model(input)


class DepthModel(nn.Module):
    def __init__(self, encoder):
        super(DepthModel, self).__init__()
        if encoder == "resnet50_stride32":
            self.encoder_modules = network.resnet50_stride32()
        elif encoder == "resnext101_stride32x8d":
            self.encoder_modules = network.resnext101_stride32x8d()
        else:
            backbone = network.__name__.split('.')[-1] + '.' + encoder
            self.encoder_modules = get_func(backbone)()
        self.decoder_modules = network.Decoder()

    def forward(self, x):
        lateral_out = self.encoder_modules(x)
        return self.decoder_modules(lateral_out)