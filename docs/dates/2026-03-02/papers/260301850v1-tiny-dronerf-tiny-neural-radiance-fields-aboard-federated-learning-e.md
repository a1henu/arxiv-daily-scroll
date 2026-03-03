---
layout: default
title: Tiny-DroNeRF: Tiny Neural Radiance Fields aboard Federated Learning-enabled Nano-drones
---

# Tiny-DroNeRF: Tiny Neural Radiance Fields aboard Federated Learning-enabled Nano-drones
**arXiv**：[2603.01850v1](https://arxiv.org/abs/2603.01850) · [PDF](https://arxiv.org/pdf/2603.01850.pdf)  
**作者**：Ilenia Carboni, Elia Cereda, Lorenzo Lamberti, Daniele Malpetti, Francesco Conti, Daniele Palossi  

**一句话要点**：提出Tiny-DroNeRF结合联邦学习，在资源受限的纳米无人机上实现轻量级神经辐射场训练与3D重建。

**关键词**：神经辐射场, 纳米无人机, 联邦学习, 轻量级模型, 3D重建, 超低功耗MCU

## 3 点简述
- 纳米无人机资源受限，难以运行传统NeRF模型进行3D场景重建。
- 基于Instant-NGP优化，Tiny-DroNeRF大幅减少内存占用，并利用联邦学习分布式训练。
- 实验显示内存减少96%，精度下降5.7 dB，联邦学习提升整体重建精度。

## 摘要（原文）

> Sub-30g nano-sized aerial robots can leverage their agility and form factor to autonomously explore cluttered and narrow environments, like in industrial inspection and search and rescue missions. However, the price for their tiny size is a strong limit in their resources, i.e., sub-100 mW microcontroller units (MCUs) delivering $\sim$100 GOps/s at best, and memory budgets well below 100 MB. Despite these strict constraints, we aim to enable complex vision-based tasks aboard nano-drones, such as dense 3D scene reconstruction: a key robotic task underlying fundamental capabilities like spatial awareness and motion planning. Top-performing 3D reconstruction methods leverage neural radiance fields (NeRF) models, which require GBs of memory and massive computation, usually delivered by high-end GPUs consuming 100s of Watts. Our work introduces Tiny-DroNeRF, a lightweight NeRF model, based on Instant-NGP, and optimized for running on a GAP9 ultra-low-power (ULP) MCU aboard our nano-drones. Then, we further empower our Tiny-DroNeRF by leveraging a collaborative federated learning scheme, which distributes the model training among multiple nano-drones. Our experimental results show a 96% reduction in Tiny-DroNeRF's memory footprint compared to Instant-NGP, with only a 5.7 dB drop in reconstruction accuracy. Finally, our federated learning scheme allows Tiny-DroNeRF to train with an amount of data otherwise impossible to keep in a single drone's memory, increasing the overall reconstruction accuracy. Ultimately, our work combines, for the first time, NeRF training on an ULP MCU with federated learning on nano-drones.

