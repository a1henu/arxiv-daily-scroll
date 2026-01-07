---
layout: default
title: DreamLoop: Controllable Cinemagraph Generation from a Single Photograph
---

# DreamLoop: Controllable Cinemagraph Generation from a Single Photograph
**arXiv**：[2601.02646v1](https://arxiv.org/abs/2601.02646) · [PDF](https://arxiv.org/pdf/2601.02646.pdf)  
**作者**：Aniruddha Mahapatra, Long Mai, Cusuh Ham, Feng Liu  

**一句话要点**：提出DreamLoop框架，从单张照片生成可控电影循环，无需专门训练数据。

**关键词**：电影循环生成, 可控视频合成, 视频扩散模型, 单图像动画, 时间桥接, 运动条件化

## 3 点简述
- 核心问题：现有方法难以从单张照片生成可控、无缝循环的电影循环，受限于简单运动或缺乏专门数据。
- 方法要点：通过训练视频扩散模型实现时间桥接和运动条件化，利用输入图像作为首尾帧条件强制循环，并基于静态轨迹和用户指定路径控制动画。
- 实验或效果：方法能生成高质量、复杂电影循环，优于现有方法，支持通用场景的灵活直观控制。

## 摘要（原文）

> Cinemagraphs, which combine static photographs with selective, looping motion, offer unique artistic appeal. Generating them from a single photograph in a controllable manner is particularly challenging. Existing image-animation techniques are restricted to simple, low-frequency motions and operate only in narrow domains with repetitive textures like water and smoke. In contrast, large-scale video diffusion models are not tailored for cinemagraph constraints and lack the specialized data required to generate seamless, controlled loops. We present DreamLoop, a controllable video synthesis framework dedicated to generating cinemagraphs from a single photo without requiring any cinemagraph training data. Our key idea is to adapt a general video diffusion model by training it on two objectives: temporal bridging and motion conditioning. This strategy enables flexible cinemagraph generation. During inference, by using the input image as both the first- and last- frame condition, we enforce a seamless loop. By conditioning on static tracks, we maintain a static background. Finally, by providing a user-specified motion path for a target object, our method provides intuitive control over the animation's trajectory and timing. To our knowledge, DreamLoop is the first method to enable cinemagraph generation for general scenes with flexible and intuitive controls. We demonstrate that our method produces high-quality, complex cinemagraphs that align with user intent, outperforming existing approaches.

