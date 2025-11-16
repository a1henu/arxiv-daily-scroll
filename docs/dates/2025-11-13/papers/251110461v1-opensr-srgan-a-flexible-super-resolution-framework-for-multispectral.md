---
layout: default
title: OpenSR-SRGAN: A Flexible Super-Resolution Framework for Multispectral Earth Observation Data
---

# OpenSR-SRGAN: A Flexible Super-Resolution Framework for Multispectral Earth Observation Data
**arXiv**：[2511.10461v1](https://arxiv.org/abs/2511.10461) · [PDF](https://arxiv.org/pdf/2511.10461.pdf)  
**作者**：Simon Donike, Cesar Aybar, Julio Contreras, Luis Gómez-Chova  

**一句话要点**：提出OpenSR-SRGAN框架以简化多光谱地球观测数据的超分辨率处理

**关键词**：超分辨率, 地球观测, SRGAN, 多光谱数据, 配置驱动框架, 遥感应用

## 3 点简述
- 核心问题：多光谱卫星数据（如Sentinel-2）的单图像超分辨率处理复杂且难以配置。
- 方法要点：通过配置文件统一实现SRGAN风格模型，支持生成器、判别器和损失函数的灵活切换。
- 实验或效果：提供即用配置和默认设置，降低研究人员实验和部署超分辨率管道的门槛。

## 摘要（原文）

> We present OpenSR-SRGAN, an open and modular framework for single-image super-resolution in Earth Observation. The software provides a unified implementation of SRGAN-style models that is easy to configure, extend, and apply to multispectral satellite data such as Sentinel-2. Instead of requiring users to modify model code, OpenSR-SRGAN exposes generators, discriminators, loss functions, and training schedules through concise configuration files, making it straightforward to switch between architectures, scale factors, and band setups. The framework is designed as a practical tool and benchmark implementation rather than a state-of-the-art model. It ships with ready-to-use configurations for common remote sensing scenarios, sensible default settings for adversarial training, and built-in hooks for logging, validation, and large-scene inference. By turning GAN-based super-resolution into a configuration-driven workflow, OpenSR-SRGAN lowers the entry barrier for researchers and practitioners who wish to experiment with SRGANs, compare models in a reproducible way, and deploy super-resolution pipelines across diverse Earth-observation datasets.

