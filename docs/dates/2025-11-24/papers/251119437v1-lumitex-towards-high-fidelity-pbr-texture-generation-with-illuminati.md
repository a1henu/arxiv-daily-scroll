---
layout: default
title: LumiTex: Towards High-Fidelity PBR Texture Generation with Illumination Context
---

# LumiTex: Towards High-Fidelity PBR Texture Generation with Illumination Context
**arXiv**：[2511.19437v1](https://arxiv.org/abs/2511.19437) · [PDF](https://arxiv.org/pdf/2511.19437.pdf)  
**作者**：Jingzhi Bao, Hongze Chen, Lingting Zhu, Chenyu Liu, Runze Zhang, Keyang Luo, Zeyu Hu, Weikai Chen, Yingda Yin, Xin Wang, Zehong Lin, Jun Zhang, Xiaoguang Han  

**一句话要点**：提出LumiTex框架以解决PBR纹理生成中的材料分解和纹理完成问题

**关键词**：PBR纹理生成, 材料分解, 光照感知, 纹理完成, 多分支生成, 几何引导修复

## 3 点简述
- 核心问题：现有方法难以从图像提示中分解材料并实现无缝纹理完成
- 方法要点：采用多分支生成、光照感知注意力和几何引导修复模块
- 实验或效果：在纹理质量上超越现有开源和商业方法，达到先进水平

## 摘要（原文）

> Physically-based rendering (PBR) provides a principled standard for realistic material-lighting interactions in computer graphics. Despite recent advances in generating PBR textures, existing methods fail to address two fundamental challenges: 1) materials decomposition from image prompts under limited illumination cues, and 2) seamless and view-consistent texture completion. To this end, we propose LumiTex, an end-to-end framework that comprises three key components: (1) a multi-branch generation scheme that disentangles albedo and metallic-roughness under shared illumination priors for robust material understanding, (2) a lighting-aware material attention mechanism that injects illumination context into the decoding process for physically grounded generation of albedo, metallic, and roughness maps, and (3) a geometry-guided inpainting module based on a large view synthesis model that enriches texture coverage and ensures seamless, view-consistent UV completion. Extensive experiments demonstrate that LumiTex achieves state-of-the-art performance in texture quality, surpassing both existing open-source and commercial methods.

