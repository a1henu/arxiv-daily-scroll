---
layout: default
title: Estimation of Segmental Longitudinal Strain in Transesophageal Echocardiography by Deep Learning
---

# Estimation of Segmental Longitudinal Strain in Transesophageal Echocardiography by Deep Learning
**arXiv**：[2511.02210v1](https://arxiv.org/abs/2511.02210) · [PDF](https://arxiv.org/pdf/2511.02210.pdf)  
**作者**：Anders Austlid Taskén, Thierry Judge, Erik Andreas Rye Berg, Jinyang Yu, Bjørnar Grenne, Frank Lindseth, Svend Aakhus, Pierre-Marc Jodoin, Nicolas Duchateau, Olivier Bernard, Gabriel Kiss  

**一句话要点**：提出autoStrain深度学习管道，自动估计经食管超声心动图中的节段纵向应变。

**关键词**：深度学习, 运动估计, 经食管超声心动图, 节段纵向应变, 合成数据, 临床验证

## 3 点简述
- 核心问题：节段纵向应变评估左心室功能需手动操作，效率低且资源密集。
- 方法要点：比较TeeFlow和TeeTracker两种深度学习模型，基于合成TEE数据集训练。
- 实验或效果：TeeTracker在合成数据上误差0.65毫米，临床验证与参考一致。

## 摘要（原文）

> Segmental longitudinal strain (SLS) of the left ventricle (LV) is an
> important prognostic indicator for evaluating regional LV dysfunction, in
> particular for diagnosing and managing myocardial ischemia. Current techniques
> for strain estimation require significant manual intervention and expertise,
> limiting their efficiency and making them too resource-intensive for monitoring
> purposes. This study introduces the first automated pipeline, autoStrain, for
> SLS estimation in transesophageal echocardiography (TEE) using deep learning
> (DL) methods for motion estimation. We present a comparative analysis of two DL
> approaches: TeeFlow, based on the RAFT optical flow model for dense
> frame-to-frame predictions, and TeeTracker, based on the CoTracker point
> trajectory model for sparse long-sequence predictions.
>   As ground truth motion data from real echocardiographic sequences are hardly
> accessible, we took advantage of a unique simulation pipeline (SIMUS) to
> generate a highly realistic synthetic TEE (synTEE) dataset of 80 patients with
> ground truth myocardial motion to train and evaluate both models. Our
> evaluation shows that TeeTracker outperforms TeeFlow in accuracy, achieving a
> mean distance error in motion estimation of 0.65 mm on a synTEE test dataset.
>   Clinical validation on 16 patients further demonstrated that SLS estimation
> with our autoStrain pipeline aligned with clinical references, achieving a mean
> difference (95\% limits of agreement) of 1.09% (-8.90% to 11.09%).
> Incorporation of simulated ischemia in the synTEE data improved the accuracy of
> the models in quantifying abnormal deformation. Our findings indicate that
> integrating AI-driven motion estimation with TEE can significantly enhance the
> precision and efficiency of cardiac function assessment in clinical settings.

