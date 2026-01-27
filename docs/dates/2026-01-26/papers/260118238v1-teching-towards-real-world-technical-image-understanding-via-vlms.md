---
layout: default
title: TechING: Towards Real World Technical Image Understanding via VLMs
---

# TechING: Towards Real World Technical Image Understanding via VLMs
**arXiv**：[2601.18238v1](https://arxiv.org/abs/2601.18238) · [PDF](https://arxiv.org/pdf/2601.18238.pdf)  
**作者**：Tafazzul Nadeem, Bhavik Shangari, Manish Rai, Gagan Raj Gupta, Ashutosh Modi  

**一句话要点**：提出TechING方法，通过合成数据集训练VLM以提升现实世界手绘技术图理解能力。

**关键词**：技术图理解, 视觉语言模型, 合成数据集, 自监督学习, 手绘图像, 模型微调

## 3 点简述
- 核心问题：现有VLM难以理解手绘技术图，缺乏大规模真实训练数据。
- 方法要点：构建合成数据集模拟真实图像，引入自监督任务微调Llama模型。
- 实验或效果：在合成和真实图像上显著提升性能，人类评估显示编译错误最少。

## 摘要（原文）

> Professionals working in technical domain typically hand-draw (on whiteboard, paper, etc.) technical diagrams (e.g., flowcharts, block diagrams, etc.) during discussions; however, if they want to edit these later, it needs to be drawn from scratch. Modern day VLMs have made tremendous progress in image understanding but they struggle when it comes to understanding technical diagrams. One way to overcome this problem is to fine-tune on real world hand-drawn images, but it is not practically possible to generate large number of such images. In this paper, we introduce a large synthetically generated corpus (reflective of real world images) for training VLMs and subsequently evaluate VLMs on a smaller corpus of hand-drawn images (with the help of humans). We introduce several new self-supervision tasks for training and perform extensive experiments with various baseline models and fine-tune Llama 3.2 11B-instruct model on synthetic images on these tasks to obtain LLama-VL-TUG, which significantly improves the ROUGE-L performance of Llama 3.2 11B-instruct by 2.14x and achieves the best all-round performance across all baseline models. On real-world images, human evaluation reveals that we achieve minimum compilation errors across all baselines in 7 out of 8 diagram types and improve the average F1 score of Llama 3.2 11B-instruct by 6.97x.

