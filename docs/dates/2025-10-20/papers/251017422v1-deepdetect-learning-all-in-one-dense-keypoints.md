---
layout: default
title: DeepDetect: Learning All-in-One Dense Keypoints
---

# DeepDetect: Learning All-in-One Dense Keypoints
**arXiv**：[2510.17422v1](https://arxiv.org/abs/2510.17422) · [PDF](https://arxiv.org/pdf/2510.17422.pdf)  
**作者**：Shaharyar Ahmed Khan Tareen, Filza Khan Tareen  

**一句话要点**：提出DeepDetect以解决关键点检测在密度、重复性和适应性方面的不足

**关键词**：关键点检测, 深度学习, 密集检测, 语义理解, 图像配准, 3D重建

## 3 点简述
- 关键点检测存在对光照变化敏感、密度低、重复性差及缺乏语义理解等问题
- 融合多种检测器输出生成真值掩码，训练轻量ESPNet模型实现语义感知的密集关键点检测
- 在牛津数据集上评估，关键点密度、重复性和正确匹配数均优于现有方法

## 摘要（原文）

> Keypoint detection is the foundation of many computer vision tasks, including
> image registration, structure-from motion, 3D reconstruction, visual odometry,
> and SLAM. Traditional detectors (SIFT, SURF, ORB, BRISK, etc.) and learning
> based methods (SuperPoint, R2D2, LF-Net, D2-Net, etc.) have shown strong
> performance yet suffer from key limitations: sensitivity to photometric
> changes, low keypoint density and repeatability, limited adaptability to
> challenging scenes, and lack of semantic understanding, often failing to
> prioritize visually important regions. We present DeepDetect, an intelligent,
> all-in-one, dense keypoint detector that unifies the strengths of classical
> detectors using deep learning. Firstly, we create ground-truth masks by fusing
> outputs of 7 keypoint and 2 edge detectors, extracting diverse visual cues from
> corners and blobs to prominent edges and textures in the images. Afterwards, a
> lightweight and efficient model: ESPNet, is trained using these masks as
> labels, enabling DeepDetect to focus semantically on images while producing
> highly dense keypoints, that are adaptable to diverse and visually degraded
> conditions. Evaluations on the Oxford Affine Covariant Regions dataset
> demonstrate that DeepDetect surpasses other detectors in keypoint density,
> repeatability, and the number of correct matches, achieving maximum values of
> 0.5143 (average keypoint density), 0.9582 (average repeatability), and 59,003
> (correct matches).

