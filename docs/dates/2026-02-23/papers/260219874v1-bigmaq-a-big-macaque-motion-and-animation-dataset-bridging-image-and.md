---
layout: default
title: BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations
---

# BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations
**arXiv**：[2602.19874v1](https://arxiv.org/abs/2602.19874) · [PDF](https://arxiv.org/pdf/2602.19874.pdf)  
**作者**：Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  

**一句话要点**：提出BigMaQ数据集，通过3D姿态形状表示提升非人灵长类动物行为识别性能

**关键词**：3D姿态重建, 动物行为识别, 非人灵长类数据集, 表面跟踪, 动作识别基准, 虚拟形象建模

## 3 点简述
- 核心问题：非人灵长类动物行为识别中，现有方法缺乏准确的3D姿态形状重建，限制动作动态捕捉
- 方法要点：构建大规模猕猴交互场景数据集，使用特定主体纹理化虚拟形象，提供比现有表面跟踪方法更准确的3D姿态描述
- 实验或效果：结合姿态描述符，在动作识别基准上显著提升平均精度均值，验证姿态信息有效性

## 摘要（原文）

> The recognition of dynamic and social behavior in animals is fundamental for advancing ethology, ecology, medicine and neuroscience. Recent progress in deep learning has enabled automated behavior recognition from video, yet an accurate reconstruction of the three-dimensional (3D) pose and shape has not been integrated into this process. Especially for non-human primates, mesh-based tracking efforts lag behind those for other species, leaving pose descriptions restricted to sparse keypoints that are unable to fully capture the richness of action dynamics. To address this gap, we introduce the $\textbf{Big Ma}$ca$\textbf{Q}$ue 3D Motion and Animation Dataset ($\texttt{BigMaQ}$), a large-scale dataset comprising more than 750 scenes of interacting rhesus macaques with detailed 3D pose descriptions. Extending previous surface-based animal tracking methods, we construct subject-specific textured avatars by adapting a high-quality macaque template mesh to individual monkeys. This allows us to provide pose descriptions that are more accurate than previous state-of-the-art surface-based animal tracking methods. From the original dataset, we derive BigMaQ500, an action recognition benchmark that links surface-based pose vectors to single frames across multiple individual monkeys. By pairing features extracted from established image and video encoders with and without our pose descriptors, we demonstrate substantial improvements in mean average precision (mAP) when pose information is included. With these contributions, $\texttt{BigMaQ}$ establishes the first dataset that both integrates dynamic 3D pose-shape representations into the learning task of animal action recognition and provides a rich resource to advance the study of visual appearance, posture, and social interaction in non-human primates. The code and data are publicly available at https://martinivis.github.io/BigMaQ/ .

