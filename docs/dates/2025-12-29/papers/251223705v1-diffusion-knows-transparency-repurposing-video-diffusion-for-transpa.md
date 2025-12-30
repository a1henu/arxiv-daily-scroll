---
layout: default
title: Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation
---

# Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation
**arXiv**：[2512.23705v1](https://arxiv.org/abs/2512.23705) · [PDF](https://arxiv.org/pdf/2512.23705.pdf)  
**作者**：Shaocong Xu, Songlin Wei, Qizhe Wei, Zheng Geng, Hong Li, Licheng Shen, Qianpu Sun, Shu Han, Bin Ma, Bohan Li, Chongjie Ye, Yuhang Zheng, Nan Wang, Saining Zhang, Hao Zhao  

**一句话要点**：提出DKT模型，利用视频扩散模型重用于透明物体深度与法线估计，提升感知鲁棒性。

**关键词**：透明物体感知, 视频扩散模型, 深度估计, 法线估计, 零样本学习, 合成数据集

## 3 点简述
- 透明物体因折射、反射导致传统深度估计方法失效，产生空洞与不稳定结果。
- 基于视频扩散模型，通过LoRA适配器学习RGB到深度/法线的视频翻译，结合合成数据集训练。
- 在真实与合成视频基准上实现零样本SOTA，提升准确性与时间一致性，并应用于抓取任务。

## 摘要（原文）

> Transparent objects remain notoriously hard for perception systems: refraction, reflection and transmission break the assumptions behind stereo, ToF and purely discriminative monocular depth, causing holes and temporally unstable estimates. Our key observation is that modern video diffusion models already synthesize convincing transparent phenomena, suggesting they have internalized the optical rules. We build TransPhy3D, a synthetic video corpus of transparent/reflective scenes: 11k sequences rendered with Blender/Cycles. Scenes are assembled from a curated bank of category-rich static assets and shape-rich procedural assets paired with glass/plastic/metal materials. We render RGB + depth + normals with physically based ray tracing and OptiX denoising. Starting from a large video diffusion model, we learn a video-to-video translator for depth (and normals) via lightweight LoRA adapters. During training we concatenate RGB and (noisy) depth latents in the DiT backbone and co-train on TransPhy3D and existing frame-wise synthetic datasets, yielding temporally consistent predictions for arbitrary-length input videos. The resulting model, DKT, achieves zero-shot SOTA on real and synthetic video benchmarks involving transparency: ClearPose, DREDS (CatKnown/CatNovel), and TransPhy3D-Test. It improves accuracy and temporal consistency over strong image/video baselines, and a normal variant sets the best video normal estimation results on ClearPose. A compact 1.3B version runs at ~0.17 s/frame. Integrated into a grasping stack, DKT's depth boosts success rates across translucent, reflective and diffuse surfaces, outperforming prior estimators. Together, these results support a broader claim: "Diffusion knows transparency." Generative video priors can be repurposed, efficiently and label-free, into robust, temporally coherent perception for challenging real-world manipulation.

