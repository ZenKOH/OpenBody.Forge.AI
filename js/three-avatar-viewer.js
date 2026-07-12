/*
OpenBody Forge AI Three.js integration adapter.

This lightweight placeholder gives the repository a stable browser-runtime contract
before real GLB assets are committed. In production, load Three.js, GLTFLoader
and AnimationMixer, then bind manifest animation clip names to app controls.
*/

export const OpenBodyRuntimeContract = {
  avatarPath: "assets/3d/adult_neutral.glb",
  manifestPath: "assets/3d/manifest.json",
  requiredControls: ["play", "pause", "stop", "replay", "voiceToggle", "fallback"],
  requiredClips: ["squat", "lunge", "bridge", "push", "plank", "deadbug", "balance", "cardio", "stretch", "inchworm", "burpee", "calf", "row"]
};
