---
layout: default
title: Adding internal audio sensing to internal vision enables human-like in-hand fabric recognition with soft robotic fingertips
---

# Adding internal audio sensing to internal vision enables human-like in-hand fabric recognition with soft robotic fingertips
**arXiv**：[2602.12918v1](https://arxiv.org/abs/2602.12918) · [PDF](https://arxiv.org/pdf/2602.12918.pdf)  
**作者**：Iris Andrussow, Jans Solano, Benjamin A. Richardson, Georg Martius, Katherine J. Kuchenbecker  

**一句话要点**：提出集成内部音频与视觉传感的软体机器人指尖系统，实现类人触觉织物识别。

**关键词**：机器人触觉感知, 软体机器人指尖, 音频-视觉传感, 织物识别, Transformer模型, 触觉表征学习

## 3 点简述
- 核心问题：机器人触觉传感器难以同时实现高空间分辨率与高时间采样率，限制织物感知能力。
- 方法要点：结合Minsight视觉传感器（50 Hz）与Minsound音频传感器（50 Hz–15 kHz），模拟人类指尖触觉整合。
- 实验或效果：基于Transformer的方法在20种常见织物数据集上达到97%分类准确率，并学习织物拉伸性、厚度和粗糙度表征。

## 摘要（原文）

> Distinguishing the feel of smooth silk from coarse cotton is a trivial everyday task for humans. When exploring such fabrics, fingertip skin senses both spatio-temporal force patterns and texture-induced vibrations that are integrated to form a haptic representation of the explored material. It is challenging to reproduce this rich, dynamic perceptual capability in robots because tactile sensors typically cannot achieve both high spatial resolution and high temporal sampling rate. In this work, we present a system that can sense both types of haptic information, and we investigate how each type influences robotic tactile perception of fabrics. Our robotic hand's middle finger and thumb each feature a soft tactile sensor: one is the open-source Minsight sensor that uses an internal camera to measure fingertip deformation and force at 50 Hz, and the other is our new sensor Minsound that captures vibrations through an internal MEMS microphone with a bandwidth from 50 Hz to 15 kHz. Inspired by the movements humans make to evaluate fabrics, our robot actively encloses and rubs folded fabric samples between its two sensitive fingers. Our results test the influence of each sensing modality on overall classification performance, showing high utility for the audio-based sensor. Our transformer-based method achieves a maximum fabric classification accuracy of 97 % on a dataset of 20 common fabrics. Incorporating an external microphone away from Minsound increases our method's robustness in loud ambient noise conditions. To show that this audio-visual tactile sensing approach generalizes beyond the training data, we learn general representations of fabric stretchiness, thickness, and roughness.

