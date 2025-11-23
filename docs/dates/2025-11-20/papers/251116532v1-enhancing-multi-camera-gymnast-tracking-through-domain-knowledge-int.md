---
layout: default
title: Enhancing Multi-Camera Gymnast Tracking Through Domain Knowledge Integration
---

# Enhancing Multi-Camera Gymnast Tracking Through Domain Knowledge Integration
**arXiv**：[2511.16532v1](https://arxiv.org/abs/2511.16532) · [PDF](https://arxiv.org/pdf/2511.16532.pdf)  
**作者**：Fan Yang, Shigeyuki Odashima, Shoichi Masui, Ikuo Kusajima, Sosuke Yamao, Shan Jiang  

**一句话要点**：提出结合领域知识的多相机体操运动员跟踪方法，以应对检测不足问题。

**关键词**：多相机跟踪, 体操运动员跟踪, 领域知识集成, 数据关联, 3D轨迹估计, 射线平面相交

## 3 点简述
- 核心问题：体操馆相机数量有限，检测易受光照、遮挡影响，导致多视角检测不足。
- 方法要点：引入体操领域知识，使用射线-平面相交生成共面3D轨迹候选，补偿不确定轨迹。
- 实验或效果：在体操世界锦标赛中成功应用，验证方法在挑战性场景下优于现有方法。

## 摘要（原文）

> We present a robust multi-camera gymnast tracking, which has been applied at international gymnastics championships for gymnastics judging. Despite considerable progress in multi-camera tracking algorithms, tracking gymnasts presents unique challenges: (i) due to space restrictions, only a limited number of cameras can be installed in the gymnastics stadium; and (ii) due to variations in lighting, background, uniforms, and occlusions, multi-camera gymnast detection may fail in certain views and only provide valid detections from two opposing views. These factors complicate the accurate determination of a gymnast's 3D trajectory using conventional multi-camera triangulation. To alleviate this issue, we incorporate gymnastics domain knowledge into our tracking solution. Given that a gymnast's 3D center typically lies within a predefined vertical plane during \revised{much of their} performance, we can apply a ray-plane intersection to generate coplanar 3D trajectory candidates for opposing-view detections. More specifically, we propose a novel cascaded data association (DA) paradigm that employs triangulation to generate 3D trajectory candidates when cross-view detections are sufficient, and resort to the ray-plane intersection when they are insufficient. Consequently, coplanar candidates are used to compensate for uncertain trajectories, thereby minimizing tracking failures. The robustness of our method is validated through extensive experimentation, demonstrating its superiority over existing methods in challenging scenarios. Furthermore, our gymnastics judging system, equipped with this tracking method, has been successfully applied to recent Gymnastics World Championships, earning significant recognition from the International Gymnastics Federation.

