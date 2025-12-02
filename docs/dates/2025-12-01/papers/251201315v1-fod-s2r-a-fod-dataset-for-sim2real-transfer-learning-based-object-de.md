---
layout: default
title: FOD-S2R: A FOD Dataset for Sim2Real Transfer Learning based Object Detection
---

# FOD-S2R: A FOD Dataset for Sim2Real Transfer Learning based Object Detection
**arXiv**：[2512.01315v1](https://arxiv.org/abs/2512.01315) · [PDF](https://arxiv.org/pdf/2512.01315.pdf)  
**作者**：Ashish Vashist, Qiranul Saadiyean, Suresh Sundaram, Chandra Sekhar Seelamantula  

**一句话要点**：提出FOD-S2R数据集以解决飞机油箱内异物检测的模拟到真实迁移学习问题

**关键词**：异物检测, 模拟到真实迁移学习, 合成数据增强, 封闭环境视觉, 飞机维护, 目标检测数据集

## 3 点简述
- 核心问题：飞机油箱内异物检测缺乏针对封闭环境的专用数据集，存在安全风险。
- 方法要点：构建包含真实与合成图像的FOD-S2R数据集，首次系统评估合成数据在封闭结构中的有效性。
- 实验或效果：基准测试显示合成数据提升检测精度和泛化能力，缩小模拟到真实差距。

## 摘要（原文）

> Foreign Object Debris (FOD) within aircraft fuel tanks presents critical safety hazards including fuel contamination, system malfunctions, and increased maintenance costs. Despite the severity of these risks, there is a notable lack of dedicated datasets for the complex, enclosed environments found inside fuel tanks. To bridge this gap, we present a novel dataset, FOD-S2R, composed of real and synthetic images of the FOD within a simulated aircraft fuel tank. Unlike existing datasets that focus on external or open-air environments, our dataset is the first to systematically evaluate the effectiveness of synthetic data in enhancing the real-world FOD detection performance in confined, closed structures. The real-world subset consists of 3,114 high-resolution HD images captured in a controlled fuel tank replica, while the synthetic subset includes 3,137 images generated using Unreal Engine. The dataset is composed of various Field of views (FOV), object distances, lighting conditions, color, and object size. Prior research has demonstrated that synthetic data can reduce reliance on extensive real-world annotations and improve the generalizability of vision models. Thus, we benchmark several state-of-the-art object detection models and demonstrate that introducing synthetic data improves the detection accuracy and generalization to real-world conditions. These experiments demonstrate the effectiveness of synthetic data in enhancing the model performance and narrowing the Sim2Real gap, providing a valuable foundation for developing automated FOD detection systems for aviation maintenance.

