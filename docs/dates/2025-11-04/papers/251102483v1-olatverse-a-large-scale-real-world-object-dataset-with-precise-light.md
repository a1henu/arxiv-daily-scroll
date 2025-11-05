---
layout: default
title: OLATverse: A Large-scale Real-world Object Dataset with Precise Lighting Control
---

# OLATverse: A Large-scale Real-world Object Dataset with Precise Lighting Control
**arXiv**：[2511.02483v1](https://arxiv.org/abs/2511.02483) · [PDF](https://arxiv.org/pdf/2511.02483.pdf)  
**作者**：Xilong Zhou, Jianchun Chen, Pramod Rao, Timo Teufel, Linjie Lyu, Tigran Minasian, Oleksandr Sotnychenko, Xiaoxiao Long, Marc Habermann, Christian Theobalt  

**一句话要点**：提出OLATverse大规模真实物体数据集，以解决逆渲染和重光照方法对合成数据依赖的问题。

**关键词**：逆渲染, 重光照, 真实物体数据集, 光照控制, 多视角捕获, 基准评估

## 3 点简述
- 核心问题：现有逆渲染和重光照方法依赖合成数据集，限制真实性和泛化能力。
- 方法要点：包含765个真实物体，在精确控制光照下从多视角捕获约900万张图像。
- 实验或效果：提供校准相机参数、物体掩码等资源，并建立首个真实世界物体中心基准。

## 摘要（原文）

> We introduce OLATverse, a large-scale dataset comprising around 9M images of
> 765 real-world objects, captured from multiple viewpoints under a diverse set
> of precisely controlled lighting conditions. While recent advances in
> object-centric inverse rendering, novel view synthesis and relighting have
> shown promising results, most techniques still heavily rely on the synthetic
> datasets for training and small-scale real-world datasets for benchmarking,
> which limits their realism and generalization. To address this gap, OLATverse
> offers two key advantages over existing datasets: large-scale coverage of real
> objects and high-fidelity appearance under precisely controlled illuminations.
> Specifically, OLATverse contains 765 common and uncommon real-world objects,
> spanning a wide range of material categories. Each object is captured using 35
> DSLR cameras and 331 individually controlled light sources, enabling the
> simulation of diverse illumination conditions. In addition, for each object, we
> provide well-calibrated camera parameters, accurate object masks, photometric
> surface normals, and diffuse albedo as auxiliary resources. We also construct
> an extensive evaluation set, establishing the first comprehensive real-world
> object-centric benchmark for inverse rendering and normal estimation. We
> believe that OLATverse represents a pivotal step toward integrating the next
> generation of inverse rendering and relighting methods with real-world data.
> The full dataset, along with all post-processing workflows, will be publicly
> released at https://vcai.mpi-inf.mpg.de/projects/OLATverse/.

