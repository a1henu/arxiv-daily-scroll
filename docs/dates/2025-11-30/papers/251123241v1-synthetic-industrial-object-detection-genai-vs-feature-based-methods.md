---
layout: default
title: Synthetic Industrial Object Detection: GenAI vs. Feature-Based Methods
---

# Synthetic Industrial Object Detection: GenAI vs. Feature-Based Methods
**arXiv**：[2511.23241v1](https://arxiv.org/abs/2511.23241) · [PDF](https://arxiv.org/pdf/2511.23241.pdf)  
**作者**：Jose Moises Araya-Martinez, Adrián Sanchis Reig, Gautham Mohan, Sarvenaz Sardari, Jens Lambrecht, Jörg Krüger  

**一句话要点**：对比特征方法与生成式AI在工业合成目标检测中的性能，发现特征方法更优

**关键词**：合成数据生成, 域适应, 目标检测, 工业视觉, 模拟到现实

## 3 点简述
- 核心问题：工业场景中合成数据生成与标注成本高，需有效缩小模拟到现实的差距
- 方法要点：评估域随机化、域适应技术，包括特征方法、生成式AI和经典渲染，无需手动标注
- 实验或效果：在工业和机器人数据集上，特征方法如感知哈希在准确性和效率上优于生成式AI

## 摘要（原文）

> Reducing the burden of data generation and annotation remains a major challenge for the cost-effective deployment of machine learning in industrial and robotics settings. While synthetic rendering is a promising solution, bridging the sim-to-real gap often requires expert intervention. In this work, we benchmark a range of domain randomization (DR) and domain adaptation (DA) techniques, including feature-based methods, generative AI (GenAI), and classical rendering approaches, for creating contextualized synthetic data without manual annotation. Our evaluation focuses on the effectiveness and efficiency of low-level and high-level feature alignment, as well as a controlled diffusion-based DA method guided by prompts generated from real-world contexts. We validate our methods on two datasets: a proprietary industrial dataset (automotive and logistics) and a public robotics dataset. Results show that if render-based data with enough variability is available as seed, simpler feature-based methods, such as brightness-based and perceptual hashing filtering, outperform more complex GenAI-based approaches in both accuracy and resource efficiency. Perceptual hashing consistently achieves the highest performance, with mAP50 scores of 98% and 67% on the industrial and robotics datasets, respectively. Additionally, GenAI methods present significant time overhead for data generation at no apparent improvement of sim-to-real mAP values compared to simpler methods. Our findings offer actionable insights for efficiently bridging the sim-to-real gap, enabling high real-world performance from models trained exclusively on synthetic data.

