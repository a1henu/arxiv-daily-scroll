---
layout: default
title: ObjectForesight: Predicting Future 3D Object Trajectories from Human Videos
---

# ObjectForesight: Predicting Future 3D Object Trajectories from Human Videos
**arXiv**：[2601.05237v1](https://arxiv.org/abs/2601.05237) · [PDF](https://arxiv.org/pdf/2601.05237.pdf)  
**作者**：Rustin Soraki, Homanga Bharadhwaj, Ali Farhadi, Roozbeh Mottaghi  

**一句话要点**：提出ObjectForesight以从人类视频预测未来3D物体轨迹

**关键词**：3D物体轨迹预测, 自中心视频理解, 刚体动力学模型, 6自由度位姿估计, 几何一致性预测

## 3 点简述
- 核心问题：从被动视觉观察预测物体未来运动，模拟人类对物体交互的预判能力。
- 方法要点：基于3D物体中心动力学模型，从短自中心视频预测刚体6自由度位姿和轨迹。
- 实验或效果：利用大规模伪真值数据集训练，在准确性、几何一致性和泛化性上取得显著提升。

## 摘要（原文）

> Humans can effortlessly anticipate how objects might move or change through interaction--imagining a cup being lifted, a knife slicing, or a lid being closed. We aim to endow computational systems with a similar ability to predict plausible future object motions directly from passive visual observation. We introduce ObjectForesight, a 3D object-centric dynamics model that predicts future 6-DoF poses and trajectories of rigid objects from short egocentric video sequences. Unlike conventional world or dynamics models that operate in pixel or latent space, ObjectForesight represents the world explicitly in 3D at the object level, enabling geometrically grounded and temporally coherent predictions that capture object affordances and trajectories. To train such a model at scale, we leverage recent advances in segmentation, mesh reconstruction, and 3D pose estimation to curate a dataset of 2 million plus short clips with pseudo-ground-truth 3D object trajectories. Through extensive experiments, we show that ObjectForesight achieves significant gains in accuracy, geometric consistency, and generalization to unseen objects and scenes, establishing a scalable framework for learning physically grounded, object-centric dynamics models directly from observation. objectforesight.github.io

