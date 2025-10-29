---
layout: default
title: Stroke Lesion Segmentation in Clinical Workflows: A Modular, Lightweight, and Deployment-Ready Tool
---

# Stroke Lesion Segmentation in Clinical Workflows: A Modular, Lightweight, and Deployment-Ready Tool
**arXiv**：[2510.24378v1](https://arxiv.org/abs/2510.24378) · [PDF](https://arxiv.org/pdf/2510.24378.pdf)  
**作者**：Yann Kerverdo, Florent Leray, Youwan Mahé, Stéphanie Leplaideur, Francesca Galassi  

**一句话要点**：提出StrokeSeg框架，将高性能卒中病灶分割模型转化为可部署的临床应用工具。

**关键词**：卒中病灶分割, 模块化框架, ONNX Runtime, 模型量化, 临床部署, 轻量级工具

## 3 点简述
- 核心问题：nnU-Net等深度学习框架依赖重、设计单一，难以临床部署。
- 方法要点：采用模块化设计，预处理用Anima工具箱，推理用ONNX Runtime并量化模型。
- 实验或效果：在300例卒中患者数据上，分割性能与原PyTorch管道相当。

## 摘要（原文）

> Deep learning frameworks such as nnU-Net achieve state-of-the-art performance
> in brain lesion segmentation but remain difficult to deploy clinically due to
> heavy dependencies and monolithic design. We introduce \textit{StrokeSeg}, a
> modular and lightweight framework that translates research-grade stroke lesion
> segmentation models into deployable applications. Preprocessing, inference, and
> postprocessing are decoupled: preprocessing relies on the Anima toolbox with
> BIDS-compliant outputs, and inference uses ONNX Runtime with \texttt{Float16}
> quantisation, reducing model size by about 50\%. \textit{StrokeSeg} provides
> both graphical and command-line interfaces and is distributed as Python scripts
> and as a standalone Windows executable. On a held-out set of 300 sub-acute and
> chronic stroke subjects, segmentation performance was equivalent to the
> original PyTorch pipeline (Dice difference $<10^{-3}$), demonstrating that
> high-performing research pipelines can be transformed into portable, clinically
> usable tools.

