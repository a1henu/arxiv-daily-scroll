---
layout: default
title: ClothHMR: 3D Mesh Recovery of Humans in Diverse Clothing from Single Image
---

# ClothHMR: 3D Mesh Recovery of Humans in Diverse Clothing from Single Image
**arXiv**：[2512.17545v1](https://arxiv.org/abs/2512.17545) · [PDF](https://arxiv.org/pdf/2512.17545.pdf)  
**作者**：Yunqi Gao, Leyuan Liu, Yuhan Li, Changxin Gao, Yuanyuan Liu, Jingying Chen  

**一句话要点**：提出ClothHMR以从单张图像中准确恢复穿着多样服装的人体3D网格

**关键词**：3D人体网格恢复, 服装裁剪, 基础视觉模型, 单图像估计, 姿态估计, 形状估计

## 3 点简述
- 核心问题：现有方法在处理紧身衣时表现良好，但对宽松服装下的人体形状和姿态估计效果差。
- 方法要点：通过服装裁剪模块使服装贴合身体轮廓，并利用基础人类视觉模型优化3D网格参数。
- 实验或效果：在基准数据集和真实图像上显著优于现有方法，并开发了在线时尚购物应用。

## 摘要（原文）

> With 3D data rapidly emerging as an important form of multimedia information, 3D human mesh recovery technology has also advanced accordingly. However, current methods mainly focus on handling humans wearing tight clothing and perform poorly when estimating body shapes and poses under diverse clothing, especially loose garments. To this end, we make two key insights: (1) tailoring clothing to fit the human body can mitigate the adverse impact of clothing on 3D human mesh recovery, and (2) utilizing human visual information from large foundational models can enhance the generalization ability of the estimation. Based on these insights, we propose ClothHMR, to accurately recover 3D meshes of humans in diverse clothing. ClothHMR primarily consists of two modules: clothing tailoring (CT) and FHVM-based mesh recovering (MR). The CT module employs body semantic estimation and body edge prediction to tailor the clothing, ensuring it fits the body silhouette. The MR module optimizes the initial parameters of the 3D human mesh by continuously aligning the intermediate representations of the 3D mesh with those inferred from the foundational human visual model (FHVM). ClothHMR can accurately recover 3D meshes of humans wearing diverse clothing, precisely estimating their body shapes and poses. Experimental results demonstrate that ClothHMR significantly outperforms existing state-of-the-art methods across benchmark datasets and in-the-wild images. Additionally, a web application for online fashion and shopping powered by ClothHMR is developed, illustrating that ClothHMR can effectively serve real-world usage scenarios. The code and model for ClothHMR are available at: \url{https://github.com/starVisionTeam/ClothHMR}.

